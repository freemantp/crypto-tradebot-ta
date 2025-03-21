# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import privateService_pb2 as privateService__pb2


class PrivateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalances = channel.unary_unary(
                '/hft.PrivateService/GetBalances',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=privateService__pb2.BalancesResponse.FromString,
                )
        self.PlaceLimitOrder = channel.unary_unary(
                '/hft.PrivateService/PlaceLimitOrder',
                request_serializer=privateService__pb2.LimitOrderRequest.SerializeToString,
                response_deserializer=privateService__pb2.LimitOrderResponse.FromString,
                )
        self.PlaceBulkLimitOrder = channel.unary_unary(
                '/hft.PrivateService/PlaceBulkLimitOrder',
                request_serializer=privateService__pb2.BulkLimitOrderRequest.SerializeToString,
                response_deserializer=privateService__pb2.BulkLimitOrderResponse.FromString,
                )
        self.PlaceMarketOrder = channel.unary_unary(
                '/hft.PrivateService/PlaceMarketOrder',
                request_serializer=privateService__pb2.MarketOrderRequest.SerializeToString,
                response_deserializer=privateService__pb2.MarketOrderResponse.FromString,
                )
        self.GetOrder = channel.unary_unary(
                '/hft.PrivateService/GetOrder',
                request_serializer=privateService__pb2.OrderRequest.SerializeToString,
                response_deserializer=privateService__pb2.OrderResponse.FromString,
                )
        self.GetActiveOrders = channel.unary_unary(
                '/hft.PrivateService/GetActiveOrders',
                request_serializer=privateService__pb2.OrdersRequest.SerializeToString,
                response_deserializer=privateService__pb2.OrdersResponse.FromString,
                )
        self.GetClosedOrders = channel.unary_unary(
                '/hft.PrivateService/GetClosedOrders',
                request_serializer=privateService__pb2.OrdersRequest.SerializeToString,
                response_deserializer=privateService__pb2.OrdersResponse.FromString,
                )
        self.CancelAllOrders = channel.unary_unary(
                '/hft.PrivateService/CancelAllOrders',
                request_serializer=privateService__pb2.CancelOrdersRequest.SerializeToString,
                response_deserializer=privateService__pb2.CancelOrderResponse.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/hft.PrivateService/CancelOrder',
                request_serializer=privateService__pb2.CancelOrderRequest.SerializeToString,
                response_deserializer=privateService__pb2.CancelOrderResponse.FromString,
                )
        self.GetTrades = channel.unary_unary(
                '/hft.PrivateService/GetTrades',
                request_serializer=privateService__pb2.TradesRequest.SerializeToString,
                response_deserializer=privateService__pb2.TradesResponse.FromString,
                )
        self.GetOrderTrades = channel.unary_unary(
                '/hft.PrivateService/GetOrderTrades',
                request_serializer=privateService__pb2.OrderTradesRequest.SerializeToString,
                response_deserializer=privateService__pb2.TradesResponse.FromString,
                )
        self.GetBalanceUpdates = channel.unary_stream(
                '/hft.PrivateService/GetBalanceUpdates',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=privateService__pb2.BalanceUpdate.FromString,
                )
        self.GetTradeUpdates = channel.unary_stream(
                '/hft.PrivateService/GetTradeUpdates',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=privateService__pb2.TradeUpdate.FromString,
                )
        self.GetOperationsHistory = channel.unary_unary(
                '/hft.PrivateService/GetOperationsHistory',
                request_serializer=privateService__pb2.GetOperationsHistoryRequest.SerializeToString,
                response_deserializer=privateService__pb2.GetOperationsHistoryResponse.FromString,
                )
        self.CreateDepositAddresses = channel.unary_unary(
                '/hft.PrivateService/CreateDepositAddresses',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=privateService__pb2.CreateDepositAddressesResponse.FromString,
                )
        self.GetDepositAddress = channel.unary_unary(
                '/hft.PrivateService/GetDepositAddress',
                request_serializer=privateService__pb2.GetDepositAddressRequest.SerializeToString,
                response_deserializer=privateService__pb2.GetDepositAddressResponse.FromString,
                )
        self.GetDepositAddresses = channel.unary_unary(
                '/hft.PrivateService/GetDepositAddresses',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=privateService__pb2.GetDepositAddressesResponse.FromString,
                )
        self.CreateWithdrawal = channel.unary_unary(
                '/hft.PrivateService/CreateWithdrawal',
                request_serializer=privateService__pb2.CreateWithdrawalRequest.SerializeToString,
                response_deserializer=privateService__pb2.CreateWithdrawalResponse.FromString,
                )


class PrivateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBalances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaceLimitOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaceBulkLimitOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaceMarketOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActiveOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClosedOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelAllOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderTrades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBalanceUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTradeUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperationsHistory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDepositAddresses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepositAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepositAddresses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWithdrawal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalances': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalances,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=privateService__pb2.BalancesResponse.SerializeToString,
            ),
            'PlaceLimitOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceLimitOrder,
                    request_deserializer=privateService__pb2.LimitOrderRequest.FromString,
                    response_serializer=privateService__pb2.LimitOrderResponse.SerializeToString,
            ),
            'PlaceBulkLimitOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceBulkLimitOrder,
                    request_deserializer=privateService__pb2.BulkLimitOrderRequest.FromString,
                    response_serializer=privateService__pb2.BulkLimitOrderResponse.SerializeToString,
            ),
            'PlaceMarketOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceMarketOrder,
                    request_deserializer=privateService__pb2.MarketOrderRequest.FromString,
                    response_serializer=privateService__pb2.MarketOrderResponse.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=privateService__pb2.OrderRequest.FromString,
                    response_serializer=privateService__pb2.OrderResponse.SerializeToString,
            ),
            'GetActiveOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActiveOrders,
                    request_deserializer=privateService__pb2.OrdersRequest.FromString,
                    response_serializer=privateService__pb2.OrdersResponse.SerializeToString,
            ),
            'GetClosedOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClosedOrders,
                    request_deserializer=privateService__pb2.OrdersRequest.FromString,
                    response_serializer=privateService__pb2.OrdersResponse.SerializeToString,
            ),
            'CancelAllOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelAllOrders,
                    request_deserializer=privateService__pb2.CancelOrdersRequest.FromString,
                    response_serializer=privateService__pb2.CancelOrderResponse.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=privateService__pb2.CancelOrderRequest.FromString,
                    response_serializer=privateService__pb2.CancelOrderResponse.SerializeToString,
            ),
            'GetTrades': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrades,
                    request_deserializer=privateService__pb2.TradesRequest.FromString,
                    response_serializer=privateService__pb2.TradesResponse.SerializeToString,
            ),
            'GetOrderTrades': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderTrades,
                    request_deserializer=privateService__pb2.OrderTradesRequest.FromString,
                    response_serializer=privateService__pb2.TradesResponse.SerializeToString,
            ),
            'GetBalanceUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBalanceUpdates,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=privateService__pb2.BalanceUpdate.SerializeToString,
            ),
            'GetTradeUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTradeUpdates,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=privateService__pb2.TradeUpdate.SerializeToString,
            ),
            'GetOperationsHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperationsHistory,
                    request_deserializer=privateService__pb2.GetOperationsHistoryRequest.FromString,
                    response_serializer=privateService__pb2.GetOperationsHistoryResponse.SerializeToString,
            ),
            'CreateDepositAddresses': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDepositAddresses,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=privateService__pb2.CreateDepositAddressesResponse.SerializeToString,
            ),
            'GetDepositAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepositAddress,
                    request_deserializer=privateService__pb2.GetDepositAddressRequest.FromString,
                    response_serializer=privateService__pb2.GetDepositAddressResponse.SerializeToString,
            ),
            'GetDepositAddresses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepositAddresses,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=privateService__pb2.GetDepositAddressesResponse.SerializeToString,
            ),
            'CreateWithdrawal': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWithdrawal,
                    request_deserializer=privateService__pb2.CreateWithdrawalRequest.FromString,
                    response_serializer=privateService__pb2.CreateWithdrawalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hft.PrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PrivateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBalances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetBalances',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            privateService__pb2.BalancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaceLimitOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/PlaceLimitOrder',
            privateService__pb2.LimitOrderRequest.SerializeToString,
            privateService__pb2.LimitOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaceBulkLimitOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/PlaceBulkLimitOrder',
            privateService__pb2.BulkLimitOrderRequest.SerializeToString,
            privateService__pb2.BulkLimitOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaceMarketOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/PlaceMarketOrder',
            privateService__pb2.MarketOrderRequest.SerializeToString,
            privateService__pb2.MarketOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetOrder',
            privateService__pb2.OrderRequest.SerializeToString,
            privateService__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActiveOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetActiveOrders',
            privateService__pb2.OrdersRequest.SerializeToString,
            privateService__pb2.OrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClosedOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetClosedOrders',
            privateService__pb2.OrdersRequest.SerializeToString,
            privateService__pb2.OrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelAllOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/CancelAllOrders',
            privateService__pb2.CancelOrdersRequest.SerializeToString,
            privateService__pb2.CancelOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/CancelOrder',
            privateService__pb2.CancelOrderRequest.SerializeToString,
            privateService__pb2.CancelOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetTrades',
            privateService__pb2.TradesRequest.SerializeToString,
            privateService__pb2.TradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetOrderTrades',
            privateService__pb2.OrderTradesRequest.SerializeToString,
            privateService__pb2.TradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBalanceUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/hft.PrivateService/GetBalanceUpdates',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            privateService__pb2.BalanceUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTradeUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/hft.PrivateService/GetTradeUpdates',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            privateService__pb2.TradeUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperationsHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetOperationsHistory',
            privateService__pb2.GetOperationsHistoryRequest.SerializeToString,
            privateService__pb2.GetOperationsHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDepositAddresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/CreateDepositAddresses',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            privateService__pb2.CreateDepositAddressesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDepositAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetDepositAddress',
            privateService__pb2.GetDepositAddressRequest.SerializeToString,
            privateService__pb2.GetDepositAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDepositAddresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/GetDepositAddresses',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            privateService__pb2.GetDepositAddressesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWithdrawal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hft.PrivateService/CreateWithdrawal',
            privateService__pb2.CreateWithdrawalRequest.SerializeToString,
            privateService__pb2.CreateWithdrawalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
