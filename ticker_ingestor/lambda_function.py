import os
import json
import boto3
import logging
from datetime import datetime
from lykke.lykkeservice import LykkeService
from mongoservice import MongoService
from signals import OrderSignal, TrendSignal
from ta_service import TechnicalAnalysisService

CRYPTO_CURRENCY = 'BTC'
FIAT_CURRENCY = 'USD'

mongo_service = MongoService(os.environ['MONGO_HOST'], 
                             os.environ['MONGO_CREDENTIALS'], 
                             'tradebot')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    price = get_current_price(f'{CRYPTO_CURRENCY}{FIAT_CURRENCY}')
    if price:
        insert_price( datetime.fromtimestamp(price['timestamp']), price['bid'], price['ask'], f'{CRYPTO_CURRENCY}-{FIAT_CURRENCY}')

        ta_service = TechnicalAnalysisService(mongo_service)
        rsi_signal, rsi_value = ta_service.analyze_rsi()

        if rsi_signal:        
            macd_signal, macd_signal_line, macd_value = ta_service.analyze_macd()

            logger.info('RSI: signal=%s, rsi=%s', rsi_signal, rsi_value)
            logger.info('MACD: signal=%s, macdSignal=%s, macd_value=%s', macd_signal, macd_signal_line, macd_value)
                        
            buy_sell_signal = buy_sell_decision(macd_signal.signal, rsi_signal.signal) if macd_signal else None

            if buy_sell_signal:
                ref_time = min(rsi_signal.timestamp, macd_signal.timestamp)
                if not ta_service.signal_exists(buy_sell_signal, ref_time):
                    logger.info('Order: %s', buy_sell_signal)
                    ta_service.insert_signal(datetime.now(), ref_time, buy_sell_signal, price['bid'])
                    notify_order(buy_sell_signal, CRYPTO_CURRENCY, price['bid'])
    
        return {
            'statusCode': 200,
            'body': json.dumps('OK')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Could not fetch prices from upstream service')
        }
        

def insert_price(timestamp: datetime, bidPrice: float, askPrice: float, symbol: str) -> None:
    mongo_service.insert_ticker_entry(timestamp, bidPrice, askPrice, symbol)

def get_current_price(symbol: str):
    token = os.environ['LYKKE_HFT_TOKEN']
    lykke_service = LykkeService(token)
    lykke_service.is_alive()

    price = lykke_service.get_prices(symbol)
    return price

def notify_order(signal: OrderSignal, symbol, price) -> None:
    if signal:
        message = {
            "order": signal.name,
            "symbol": symbol,
            "price": price            
        }

        buy_sell_signal_topic = os.environ['ORDER_SNS_TOPIC']

        client = boto3.client('sns')
        client.publish(
            TopicArn=buy_sell_signal_topic,
            Subject=message['order'] + ' order',
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'        
        )

def buy_sell_decision(macd: TrendSignal, rsi: TrendSignal) -> OrderSignal:
  
  if rsi:
    # Check if the MACD is bullish.
    if macd == TrendSignal.MACD_BULLISH_CROSSOVER:
        # Check if the RSI is oversold.
        if rsi == TrendSignal.RSI_OVERSOLD:
        # Buy the asset.
            return OrderSignal.BUY
    else:
        # Check if the RSI is overbought.
        if rsi == TrendSignal.RSI_OVERBOUGHT:
        # Sell the asset.
            return OrderSignal.SELL

if __name__ == "__main__":
    print(lambda_handler(None,None))
 
    
    

