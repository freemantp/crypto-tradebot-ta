import json
import os
import logging

from lykke.lykkeservice import LykkeService, OrderSide

FIAT_SYMBOL = 'USD'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):

    order, symbol, price = extract_order_info(event)

    token = os.environ['LYKKE_HFT_TOKEN']
    lykke_service = LykkeService(token)

    variable_symbol = symbol if order == OrderSide.SELL else FIAT_SYMBOL
    order_pair = f'{symbol}{FIAT_SYMBOL}'

    available_balance = lykke_service.check_balance(variable_symbol)

    if available_balance > 0:        
        logger.info('Got signal to %s %s @ %s', order.value.lower(), order_pair, price)
        if order == OrderSide.BUY:
            eq_volume = lykke_service.get_asset_equivalent_volume(order_pair, available_balance, order)
            lykke_service.place_market_order(order_pair, order, eq_volume)
        elif order == OrderSide.SELL:
            lykke_service.place_market_order(order_pair, order, available_balance)
    else:
        logger.error('Can\'t %s %s @ %s. Available balance: %s %s', order.value, order_pair, price, available_balance, variable_symbol)
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }

def extract_order_info(sns_event):
    sns_message = json.loads(sns_event['Records'][0]['Sns']['Message'])
    order = OrderSide.BUY if sns_message['order'].lower() == 'buy' else (OrderSide.SELL if  sns_message['order'].lower() == 'sell' else None) 
    return order,  sns_message['symbol'], sns_message['price']


if __name__ == "__main__":
    import sys
    lambda_handler(json.loads(sys.argv[1]), None)


