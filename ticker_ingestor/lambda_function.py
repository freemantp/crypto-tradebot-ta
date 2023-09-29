import os
import json
import boto3
from datetime import datetime
from lykke.lykkeservice import LykkeService
from mongoservice import MongoService
from signals import OrderSignal, TrendSignal
from ta_service import TechnicalAnalysisService

mongo_credentials = os.environ['MONGO_CREDENTIALS']
mongo_server = os.environ['MONGO_HOST']
mongo_service = MongoService(mongo_server, mongo_credentials, 'tradebot')
buy_sell_signal_topic = 'arn:aws:sns:eu-central-2:245705525676:MacdTrendSignal'
crypto_currency = 'BTC'
fiat_currency = 'USD'

def lambda_handler(event, context):

    price = get_current_price(f'{crypto_currency}{fiat_currency}')
    insert_price( datetime.fromtimestamp(price['timestamp']), price['bid'], price['ask'], f'{crypto_currency}-{fiat_currency}')

    ta_service = TechnicalAnalysisService(mongo_service)
    rsi_signal, rsi_value = ta_service.analyze_rsi()

    if rsi_signal:        
        macd_signal, macd_signal_line, macd_value = ta_service.analyze_macd()

        print(f'{rsi_signal}, rsi={rsi_value}')
        print(f'{macd_signal}, macdSignal={macd_signal_line}, macd_value={macd_value}')
        
        buy_sell_signal = buy_sell_decision(macd_signal.signal, rsi_signal.signal) if macd_signal else None

        if buy_sell_signal:
            ref_time = min(rsi_signal.timestamp, macd_signal.timestamp)
            if not ta_service.signal_exists(buy_sell_signal, ref_time):
                print(f'Order: {buy_sell_signal}')
                ta_service.insert_signal(datetime.now(), ref_time, buy_sell_signal, price['bid'])
                notify_order(buy_sell_signal, price['bid'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }

def insert_price(timestamp: datetime, bidPrice: float, askPrice: float, symbol: str) -> None:
    mongo_service.insert_ticker_entry(timestamp, bidPrice, askPrice, symbol)

def get_current_price(symbol: str):
    token = os.environ['LYKKE_TOKEN']
    lykke_service = LykkeService(token)
    lykke_service.is_alive()

    price = lykke_service.get_prices(symbol)
    return price

def notify_order(signal: OrderSignal, price) -> None:
    if signal:
        message = {
            "order": signal.name,
            "price": price            
        }

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
    lambda_handler(None,None)
 
    
    

