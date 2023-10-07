import logging
import math
import grpc
import google.protobuf
from enum import Enum

from .lykke_api import common_pb2
from .lykke_api import isalive_pb2
from .lykke_api import isalive_pb2_grpc
from .lykke_api import privateService_pb2
from .lykke_api import publicService_pb2
from .lykke_api import privateService_pb2_grpc
from .lykke_api import publicService_pb2_grpc
from .error_handler import grpc_error_handler

class OrderSide(Enum):
    BUY = 'Buy'
    SELL = 'Sell'

class LykkeService:

    def __init__(self, access_token: str, api_endpoint: str = 'hft-apiv2-grpc.lykke.com:443') -> None:
        ssl_credentials = grpc.ssl_channel_credentials()
        token_credentials = grpc.access_token_call_credentials(access_token)
        self.credentials = grpc.composite_channel_credentials(ssl_credentials, token_credentials)
        self.api_endpoint = api_endpoint
        self.logger = logging.getLogger()


    @grpc_error_handler
    def is_alive(self):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            monitoring = isalive_pb2_grpc.MonitoringStub(channel)
            isalive = monitoring.IsAlive(isalive_pb2.IsAliveRequest())
            self.logger.info('Exchange API: %s %s', isalive.name, isalive.version)

    @grpc_error_handler
    def check_balance(self, assetId: str):
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            private_api = privateService_pb2_grpc.PrivateServiceStub(channel)
            balances = private_api.GetBalances(google.protobuf.empty_pb2.Empty())
            LykkeService._check_error(balances.error)

            balance = next((b for b in balances.payload if b.assetId==assetId), None)
            return float(balance.available) if balance else 0
                

    @staticmethod
    def _check_error(error: common_pb2.Error):
        if error.code != 0:
            logging.error(f'code: {error.code}, msg: {error.message}')

    @grpc_error_handler
    def get_prices(self, pair_id: str) -> object:

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

    @grpc_error_handler
    def get_prices_stream(self, pair_id: str):

        """pair_id: e.g BTCUSD"""
            
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            public_api = publicService_pb2_grpc.PublicServiceStub(channel)
            prices_stream = public_api.GetPriceUpdates(publicService_pb2.PriceUpdatesRequest(assetPairIds=[pair_id]))
            return prices_stream

    @grpc_error_handler
    def place_market_order(self, pair_id: str, order_side: OrderSide, volume: float):
    
        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:

            order_volume = volume
            
            if order_side == OrderSide.BUY:
                order_volume  = math.floor(volume * 10**8) / 10**8 * .995                    

            if order_volume > 0.0001: 
                private_api = privateService_pb2_grpc.PrivateServiceStub(channel)
                request = privateService_pb2.MarketOrderRequest()
                request.assetPairId = pair_id
                request.volume = '{:.8f}'.format(order_volume)
                request.side = 0 if order_side == OrderSide.BUY else 1
                self.logger.info('%sing %s %s %s', order_side.value, order_volume, pair_id)
                response = private_api.PlaceMarketOrder(request)
                self.logger.info(response)
            else:
                self.logger.error('Can\'t %s %s %s, volume must be greater than 0.0001', order_side.value, order_volume, pair_id)

    @grpc_error_handler
    def get_asset_equivalent_volume(self, asset_pair: str, volume: float, side: OrderSide):
        price = self.get_prices(asset_pair)['bid' if side == OrderSide.BUY else 'ask']
        return volume / float(price)
             
    @grpc_error_handler
    def get_asset_pairs(self):

        with grpc.secure_channel(self.api_endpoint, self.credentials) as channel:
            public_api = publicService_pb2_grpc.PublicServiceStub(channel)
            assets_response = public_api.GetAssetPairs(google.protobuf.empty_pb2.Empty())
            LykkeService._check_error(assets_response.error)
            return assets_response.payload