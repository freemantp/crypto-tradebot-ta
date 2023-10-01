import json
import os

from lykke.lykkeservice import LykkeService

def lambda_handler(event, context):


    sns_message = json.loads(event['Records'][0]['Sns']['Message'])
    order = sns_message['order']
    symbol = sns_message['symbol']
    price = sns_message['price']
    print(f'{order} {symbol} @ {price}')

    token = os.environ['LYKKE_TOKEN']
    lykke_service = LykkeService(token)
    lykke_service.check_balance()
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }

if __name__ == "__main__":
    lambda_handler(None,None)
 
    
    

