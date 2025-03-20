from lykke.lykkeservice import LykkeService
import os

token = os.environ["LYKKE_HFT_TOKEN"]


def lambda_handler(event, context):
    lykke_service = LykkeService(token)

    tx_history = [
        f"{trade['time']} {trade['side'].value} {trade['baseVolume']} {trade['baseAssetId']} ({trade['quoteVolume']} {trade['quoteAssetId']}) @ {trade['price']}"
        for trade in lykke_service.get_transactions()
    ]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": "\n".join(tx_history),
    }


if __name__ == "__main__":
    lykke_service = LykkeService(token)
    lykke_service.is_alive()
