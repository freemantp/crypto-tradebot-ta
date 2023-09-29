import logging
import grpc
import google.protobuf

from .lykke_api import common_pb2
from .lykke_api import isalive_pb2
from .lykke_api import isalive_pb2_grpc
from .lykke_api import privateService_pb2
from .lykke_api import privateService_pb2_grpc
from .lykke_api import publicService_pb2
from .lykke_api import publicService_pb2_grpc

class LykkeService:

    def __init__(self, access_token: str, api_endpoint: str = 'hft-apiv2-grpc.lykke.com:443') -> None:
        # use auth creds
        ssl_credentials = grpc.ssl_channel_credentials()
        token_credentials = grpc.access_token_call_credentials(access_token)
        self.credentials = grpc.composite_channel_credentials(ssl_credentials, token_credentials)
        self.api_endpoint = api_endpoint
        logging.basicConfig()


    def is_alive(self):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            monitoring = isalive_pb2_grpc.MonitoringStub(channel)
            isalive = monitoring.IsAlive(isalive_pb2.IsAliveRequest())
            print(f'Exchange API: {isalive.name} {isalive.version}')

    def check_balance(self):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            private_api = privateService_pb2_grpc.PrivateServiceStub(channel)
            balances = private_api.GetBalances(google.protobuf.empty_pb2.Empty())
            LykkeService._check_error(balances.error)
            print('Balances:')
            for balance in balances.payload:
                print(f'  {balance.assetId} {balance.available}')

    @staticmethod
    def _check_error(error: common_pb2.Error):
        if error.code != 0:
            logging.error(f'code: {error.code}, msg: {error.message}')

    def get_prices(self, pair_id: str):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            public_api = publicService_pb2_grpc.PublicServiceStub(channel)
            prices = public_api.GetPrices(publicService_pb2.PricesRequest(assetPairIds=[pair_id]))
            LykkeService._check_error(prices.error)
            if len(prices.payload) != 0:
               return {
                   'bid': prices.payload[0].bid,
                   'ask': prices.payload[0].ask,
                   'timestamp': prices.payload[0].timestamp.seconds,
                   'symbol': prices.payload[0].assetPairId
               }
            else:
                return None

    def print_prices(self, pair_id: str):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            public_api = publicService_pb2_grpc.PublicServiceStub(channel)
            prices_stream = public_api.GetPriceUpdates(publicService_pb2.PriceUpdatesRequest(assetPairIds=[pair_id]))

            for price in prices_stream:        
                print(price)
