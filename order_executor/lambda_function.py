import json
import os
import logging

from lykke.lykkeservice import LykkeService, OrderSide, ExchangeException

FIAT_SYMBOL = 'USD'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    order, symbol, price = extract_order_info(event)

    token = os.environ['LYKKE_HFT_TOKEN']
    lykke_service = LykkeService(token)

    variable_symbol = symbol if order == OrderSide.SELL else FIAT_SYMBOL
    order_pair = f'{symbol}{FIAT_SYMBOL}'

    available_balance = lykke_service.get_balance(variable_symbol)

    error_msg = ''

    if available_balance > 0:        
        logger.info('Got signal to %s %s @ %s', order.value.lower(), order_pair, price)
        try:
            if order == OrderSide.BUY:
                eq_volume = lykke_service.get_asset_equivalent_volume(order_pair, available_balance, order)
                result = lykke_service.place_market_order(order_pair, order, eq_volume)
            elif order == OrderSide.SELL:
                result = lykke_service.place_market_order(order_pair, order, available_balance)

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'order': order.value,
                    'symbolPair': order_pair,
                    'price' : result.price,
                    'orderId' : result.orderId
                })
            }            
        except ExchangeException as exch_excpt:
            error_msg = exch_excpt.message
    else:
        error_msg = f'Can\'t {order.value} {order_pair} @ {price}. Available balance: {available_balance} {variable_symbol}'
    
    logger.error(error_msg)
    return {
        'statusCode': 400,
        'body': json.dumps({
            'error': error_msg
        })
    }            


def extract_order_info(sns_event):
    sns_message = json.loads(sns_event['Records'][0]['Sns']['Message'])
    order = OrderSide.BUY if sns_message['order'].lower() == 'buy' else (OrderSide.SELL if  sns_message['order'].lower() == 'sell' else None) 
    return order,  sns_message['symbol'], sns_message['price']


if __name__ == "__main__":
    import sys
    r = lambda_handler(json.loads(sys.argv[1]), None)
    print(r)


