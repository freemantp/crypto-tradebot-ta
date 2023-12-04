from lykke_shared import lykkeservice
import os, json
from enum import Enum

def enum_encoder(obj):
    if isinstance(obj, Enum):
        return obj.name
    raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")


token = os.environ['LYKKE_HFT_TOKEN']
lykke_service = lykkeservice.LykkeService(token)

def get_balance():
    for trade in lykke_service.get_transactions():    
        print(f"{trade['time']} {trade['side'].value} {trade['baseVolume']} {trade['baseAssetId']} ({trade['quoteVolume']} {trade['quoteAssetId']}) @ {trade['price']}")

usd = lykke_service.get_balance('USD')
btc = lykke_service.get_balance('BTC')
print(usd)
print(btc)