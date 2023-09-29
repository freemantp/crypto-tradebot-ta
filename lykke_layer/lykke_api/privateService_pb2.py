# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: privateService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14privateService.proto\x12\x03hft\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0c\x63ommon.proto\"`\n\x11LimitOrderRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x17\n\x04side\x18\x02 \x01(\x0e\x32\t.hft.Side\x12\x0e\n\x06volume\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\"\xa8\x01\n\x15\x42ulkLimitOrderRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x1c\n\x14\x63\x61ncelPreviousOrders\x18\x02 \x01(\x08\x12%\n\ncancelMode\x18\x03 \x01(\x0e\x32\x0f.hft.CancelModeH\x00\x12\x1e\n\x06orders\x18\x04 \x03(\x0b\x32\x0e.hft.BulkOrderB\x15\n\x13optional_cancelMode\"R\n\tBulkOrder\x12\x17\n\x04side\x18\x01 \x01(\x0e\x32\t.hft.Side\x12\x0e\n\x06volume\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\t\x12\r\n\x05oldId\x18\x04 \x01(\t\"R\n\x12MarketOrderRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x17\n\x04side\x18\x02 \x01(\x0e\x32\t.hft.Side\x12\x0e\n\x06volume\x18\x03 \x01(\t\"\x1f\n\x0cOrderRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"B\n\rOrdersRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0c\n\x04take\x18\x03 \x01(\x05\"C\n\x13\x43\x61ncelOrdersRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x17\n\x04side\x18\x02 \x01(\x0e\x32\t.hft.Side\"%\n\x12\x43\x61ncelOrderRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"\xe4\x01\n\rTradesRequest\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12\x19\n\x04side\x18\x02 \x01(\x0e\x32\t.hft.SideH\x00\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x0c\n\x04take\x18\x04 \x01(\x05\x12*\n\x04\x66rom\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x12(\n\x02to\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x42\x0f\n\roptional_sideB\x0f\n\roptional_fromB\r\n\x0boptional_to\";\n\x1bGetOperationsHistoryRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\x0c\n\x04take\x18\x02 \x01(\x05\"%\n\x12OrderTradesRequest\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"S\n\x10\x42\x61lancesResponse\x12\x1d\n\x07payload\x18\x01 \x03(\x0b\x32\x0c.hft.Balance\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"\x98\x01\n\x12LimitOrderResponse\x12:\n\x07payload\x18\x01 \x01(\x0b\x32).hft.LimitOrderResponse.LimitOrderPayload\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\x1a$\n\x11LimitOrderPayload\x12\x0f\n\x07orderId\x18\x01 \x01(\t\"\xd8\x01\n\x16\x42ulkLimitOrderResponse\x12\x42\n\x07payload\x18\x01 \x01(\x0b\x32\x31.hft.BulkLimitOrderResponse.BulkLimitOrderPayload\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\x1aX\n\x15\x42ulkLimitOrderPayload\x12\x13\n\x0b\x61ssetPairId\x18\x01 \x01(\t\x12*\n\x08statuses\x18\x03 \x03(\x0b\x32\x18.hft.BulkOrderItemStatus\"f\n\x13\x42ulkOrderItemStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12$\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x15.hft.common.ErrorCode\x12\x0e\n\x06volume\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\"\xab\x01\n\x13MarketOrderResponse\x12<\n\x07payload\x18\x01 \x01(\x0b\x32+.hft.MarketOrderResponse.MarketOrderPayload\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\x1a\x34\n\x12MarketOrderPayload\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\"N\n\rOrderResponse\x12\x1b\n\x07payload\x18\x01 \x01(\x0b\x32\n.hft.Order\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"O\n\x0eOrdersResponse\x12\x1b\n\x07payload\x18\x01 \x03(\x0b\x32\n.hft.Order\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"H\n\x13\x43\x61ncelOrderResponse\x12\x0f\n\x07payload\x18\x01 \x01(\x08\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"O\n\x0eTradesResponse\x12\x1b\n\x07payload\x18\x01 \x03(\x0b\x32\n.hft.Trade\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"n\n\x07\x42\x61lance\x12\x0f\n\x07\x61ssetId\x18\x01 \x01(\t\x12\x11\n\tavailable\x18\x02 \x01(\t\x12\x10\n\x08reserved\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc3\x02\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x12lastTradeTimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x13\n\x0b\x61ssetPairId\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x17\n\x04side\x18\x07 \x01(\x0e\x32\t.hft.Side\x12\r\n\x05price\x18\x08 \x01(\t\x12\x0e\n\x06volume\x18\t \x01(\t\x12\x14\n\x0c\x66illedVolume\x18\n \x01(\t\x12\x17\n\x0fremainingVolume\x18\x0b \x01(\t\x12\x0c\n\x04\x63ost\x18\x0c \x01(\tB\x1d\n\x1boptional_lastTradeTimestamp\"\x8e\x02\n\x05Trade\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x61ssetPairId\x18\x03 \x01(\t\x12\x0f\n\x07orderId\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\t\x12\x12\n\nbaseVolume\x18\x07 \x01(\t\x12\x13\n\x0bquoteVolume\x18\x08 \x01(\t\x12\x13\n\x0b\x62\x61seAssetId\x18\t \x01(\t\x12\x14\n\x0cquoteAssetId\x18\n \x01(\t\x12\x1a\n\x03\x66\x65\x65\x18\x0b \x01(\x0b\x32\r.hft.TradeFee\x12\x17\n\x04side\x18\x0c \x01(\x0e\x32\t.hft.Side\")\n\x08TradeFee\x12\x0c\n\x04size\x18\x01 \x01(\t\x12\x0f\n\x07\x61ssetId\x18\x02 \x01(\t\"/\n\rBalanceUpdate\x12\x1e\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x0c.hft.Balance\")\n\x0bOrderUpdate\x12\x1a\n\x06orders\x18\x01 \x03(\x0b\x32\n.hft.Order\")\n\x0bTradeUpdate\x12\x1a\n\x06trades\x18\x01 \x03(\x0b\x32\n.hft.Trade\"I\n\x1cGetOperationsHistoryResponse\x12)\n\noperations\x18\x01 \x03(\x0b\x32\x15.hft.OperationHistory\"\xcd\x01\n\x10OperationHistory\x12\x13\n\x0boperationId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ssetId\x18\x02 \x01(\t\x12\x13\n\x0btotalVolume\x18\x03 \x01(\t\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x0e\x62lockchainHash\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"B\n\x1e\x43reateDepositAddressesResponse\x12 \n\x05\x65rror\x18\x01 \x01(\x0b\x32\x11.hft.common.Error\"+\n\x18GetDepositAddressRequest\x12\x0f\n\x07\x61ssetId\x18\x01 \x01(\t\"c\n\x19GetDepositAddressResponse\x12$\n\x07payload\x18\x01 \x01(\x0b\x32\x13.hft.DepositAddress\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"e\n\x1bGetDepositAddressesResponse\x12$\n\x07payload\x18\x01 \x03(\x0b\x32\x13.hft.DepositAddress\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error\"\xda\x01\n\x0e\x44\x65positAddress\x12-\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x62\x61seAddress\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x61\x64\x64ressExtension\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0f\n\x07\x61ssetId\x18\x05 \x01(\t\x12\x0e\n\x06symbol\x18\x06 \x01(\t\"\xac\x01\n\x17\x43reateWithdrawalRequest\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ssetId\x18\x02 \x01(\t\x12\x0e\n\x06volume\x18\x03 \x01(\t\x12\x1a\n\x12\x64\x65stinationAddress\x18\x04 \x01(\t\x12\x41\n\x1b\x64\x65stinationAddressExtension\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"M\n\x18\x43reateWithdrawalResponse\x12\x0f\n\x07payload\x18\x01 \x01(\t\x12 \n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hft.common.Error*\x19\n\x04Side\x12\x07\n\x03\x62uy\x10\x00\x12\x08\n\x04sell\x10\x01*H\n\nCancelMode\x12\x10\n\x0cnotEmptySide\x10\x00\x12\r\n\tbothSides\x10\x01\x12\x0c\n\x08sellSide\x10\x02\x12\x0b\n\x07\x62uySide\x10\x03*B\n\rBulkErrorCode\x12\x15\n\x11invalidInputField\x10\x00\x12\x0c\n\x08rejected\x10\x01\x12\x0c\n\x07runtime\x10\xf4\x03\x32\xff\t\n\x0ePrivateService\x12<\n\x0bGetBalances\x12\x16.google.protobuf.Empty\x1a\x15.hft.BalancesResponse\x12\x42\n\x0fPlaceLimitOrder\x12\x16.hft.LimitOrderRequest\x1a\x17.hft.LimitOrderResponse\x12N\n\x13PlaceBulkLimitOrder\x12\x1a.hft.BulkLimitOrderRequest\x1a\x1b.hft.BulkLimitOrderResponse\x12\x45\n\x10PlaceMarketOrder\x12\x17.hft.MarketOrderRequest\x1a\x18.hft.MarketOrderResponse\x12\x31\n\x08GetOrder\x12\x11.hft.OrderRequest\x1a\x12.hft.OrderResponse\x12:\n\x0fGetActiveOrders\x12\x12.hft.OrdersRequest\x1a\x13.hft.OrdersResponse\x12:\n\x0fGetClosedOrders\x12\x12.hft.OrdersRequest\x1a\x13.hft.OrdersResponse\x12\x45\n\x0f\x43\x61ncelAllOrders\x12\x18.hft.CancelOrdersRequest\x1a\x18.hft.CancelOrderResponse\x12@\n\x0b\x43\x61ncelOrder\x12\x17.hft.CancelOrderRequest\x1a\x18.hft.CancelOrderResponse\x12\x34\n\tGetTrades\x12\x12.hft.TradesRequest\x1a\x13.hft.TradesResponse\x12>\n\x0eGetOrderTrades\x12\x17.hft.OrderTradesRequest\x1a\x13.hft.TradesResponse\x12\x41\n\x11GetBalanceUpdates\x12\x16.google.protobuf.Empty\x1a\x12.hft.BalanceUpdate0\x01\x12=\n\x0fGetTradeUpdates\x12\x16.google.protobuf.Empty\x1a\x10.hft.TradeUpdate0\x01\x12[\n\x14GetOperationsHistory\x12 .hft.GetOperationsHistoryRequest\x1a!.hft.GetOperationsHistoryResponse\x12U\n\x16\x43reateDepositAddresses\x12\x16.google.protobuf.Empty\x1a#.hft.CreateDepositAddressesResponse\x12R\n\x11GetDepositAddress\x12\x1d.hft.GetDepositAddressRequest\x1a\x1e.hft.GetDepositAddressResponse\x12O\n\x13GetDepositAddresses\x12\x16.google.protobuf.Empty\x1a .hft.GetDepositAddressesResponse\x12O\n\x10\x43reateWithdrawal\x12\x1c.hft.CreateWithdrawalRequest\x1a\x1d.hft.CreateWithdrawalResponseB\x1b\xaa\x02\x18Lykke.HftApi.ApiContractb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'privateService_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\030Lykke.HftApi.ApiContract'
  _globals['_SIDE']._serialized_start=4131
  _globals['_SIDE']._serialized_end=4156
  _globals['_CANCELMODE']._serialized_start=4158
  _globals['_CANCELMODE']._serialized_end=4230
  _globals['_BULKERRORCODE']._serialized_start=4232
  _globals['_BULKERRORCODE']._serialized_end=4298
  _globals['_LIMITORDERREQUEST']._serialized_start=137
  _globals['_LIMITORDERREQUEST']._serialized_end=233
  _globals['_BULKLIMITORDERREQUEST']._serialized_start=236
  _globals['_BULKLIMITORDERREQUEST']._serialized_end=404
  _globals['_BULKORDER']._serialized_start=406
  _globals['_BULKORDER']._serialized_end=488
  _globals['_MARKETORDERREQUEST']._serialized_start=490
  _globals['_MARKETORDERREQUEST']._serialized_end=572
  _globals['_ORDERREQUEST']._serialized_start=574
  _globals['_ORDERREQUEST']._serialized_end=605
  _globals['_ORDERSREQUEST']._serialized_start=607
  _globals['_ORDERSREQUEST']._serialized_end=673
  _globals['_CANCELORDERSREQUEST']._serialized_start=675
  _globals['_CANCELORDERSREQUEST']._serialized_end=742
  _globals['_CANCELORDERREQUEST']._serialized_start=744
  _globals['_CANCELORDERREQUEST']._serialized_end=781
  _globals['_TRADESREQUEST']._serialized_start=784
  _globals['_TRADESREQUEST']._serialized_end=1012
  _globals['_GETOPERATIONSHISTORYREQUEST']._serialized_start=1014
  _globals['_GETOPERATIONSHISTORYREQUEST']._serialized_end=1073
  _globals['_ORDERTRADESREQUEST']._serialized_start=1075
  _globals['_ORDERTRADESREQUEST']._serialized_end=1112
  _globals['_BALANCESRESPONSE']._serialized_start=1114
  _globals['_BALANCESRESPONSE']._serialized_end=1197
  _globals['_LIMITORDERRESPONSE']._serialized_start=1200
  _globals['_LIMITORDERRESPONSE']._serialized_end=1352
  _globals['_LIMITORDERRESPONSE_LIMITORDERPAYLOAD']._serialized_start=1316
  _globals['_LIMITORDERRESPONSE_LIMITORDERPAYLOAD']._serialized_end=1352
  _globals['_BULKLIMITORDERRESPONSE']._serialized_start=1355
  _globals['_BULKLIMITORDERRESPONSE']._serialized_end=1571
  _globals['_BULKLIMITORDERRESPONSE_BULKLIMITORDERPAYLOAD']._serialized_start=1483
  _globals['_BULKLIMITORDERRESPONSE_BULKLIMITORDERPAYLOAD']._serialized_end=1571
  _globals['_BULKORDERITEMSTATUS']._serialized_start=1573
  _globals['_BULKORDERITEMSTATUS']._serialized_end=1675
  _globals['_MARKETORDERRESPONSE']._serialized_start=1678
  _globals['_MARKETORDERRESPONSE']._serialized_end=1849
  _globals['_MARKETORDERRESPONSE_MARKETORDERPAYLOAD']._serialized_start=1797
  _globals['_MARKETORDERRESPONSE_MARKETORDERPAYLOAD']._serialized_end=1849
  _globals['_ORDERRESPONSE']._serialized_start=1851
  _globals['_ORDERRESPONSE']._serialized_end=1929
  _globals['_ORDERSRESPONSE']._serialized_start=1931
  _globals['_ORDERSRESPONSE']._serialized_end=2010
  _globals['_CANCELORDERRESPONSE']._serialized_start=2012
  _globals['_CANCELORDERRESPONSE']._serialized_end=2084
  _globals['_TRADESRESPONSE']._serialized_start=2086
  _globals['_TRADESRESPONSE']._serialized_end=2165
  _globals['_BALANCE']._serialized_start=2167
  _globals['_BALANCE']._serialized_end=2277
  _globals['_ORDER']._serialized_start=2280
  _globals['_ORDER']._serialized_end=2603
  _globals['_TRADE']._serialized_start=2606
  _globals['_TRADE']._serialized_end=2876
  _globals['_TRADEFEE']._serialized_start=2878
  _globals['_TRADEFEE']._serialized_end=2919
  _globals['_BALANCEUPDATE']._serialized_start=2921
  _globals['_BALANCEUPDATE']._serialized_end=2968
  _globals['_ORDERUPDATE']._serialized_start=2970
  _globals['_ORDERUPDATE']._serialized_end=3011
  _globals['_TRADEUPDATE']._serialized_start=3013
  _globals['_TRADEUPDATE']._serialized_end=3054
  _globals['_GETOPERATIONSHISTORYRESPONSE']._serialized_start=3056
  _globals['_GETOPERATIONSHISTORYRESPONSE']._serialized_end=3129
  _globals['_OPERATIONHISTORY']._serialized_start=3132
  _globals['_OPERATIONHISTORY']._serialized_end=3337
  _globals['_CREATEDEPOSITADDRESSESRESPONSE']._serialized_start=3339
  _globals['_CREATEDEPOSITADDRESSESRESPONSE']._serialized_end=3405
  _globals['_GETDEPOSITADDRESSREQUEST']._serialized_start=3407
  _globals['_GETDEPOSITADDRESSREQUEST']._serialized_end=3450
  _globals['_GETDEPOSITADDRESSRESPONSE']._serialized_start=3452
  _globals['_GETDEPOSITADDRESSRESPONSE']._serialized_end=3551
  _globals['_GETDEPOSITADDRESSESRESPONSE']._serialized_start=3553
  _globals['_GETDEPOSITADDRESSESRESPONSE']._serialized_end=3654
  _globals['_DEPOSITADDRESS']._serialized_start=3657
  _globals['_DEPOSITADDRESS']._serialized_end=3875
  _globals['_CREATEWITHDRAWALREQUEST']._serialized_start=3878
  _globals['_CREATEWITHDRAWALREQUEST']._serialized_end=4050
  _globals['_CREATEWITHDRAWALRESPONSE']._serialized_start=4052
  _globals['_CREATEWITHDRAWALRESPONSE']._serialized_end=4129
  _globals['_PRIVATESERVICE']._serialized_start=4301
  _globals['_PRIVATESERVICE']._serialized_end=5580
# @@protoc_insertion_point(module_scope)
