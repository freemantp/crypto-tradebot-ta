from bson import Decimal128
from pymongo.mongo_client import MongoClient
import certifi
import logging
from datetime import datetime
from signals import OrderSignal

from ta_aggregations import macd_pipeline

class MongoService:
    def __init__(self, server: str, credentials: str, database_name: str) -> None:
        uri = f"mongodb+srv://{credentials}@{server}/?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true&w=majority&connectTimeoutMS=5000"

        self.client = MongoClient(uri, tlsCAFile=certifi.where())
        self.database_name = database_name
        logging.basicConfig()

    def ping(self) -> None:
        result = self.client.admin.command("ping")
        return "ok" in result and result["ok"] == 1

    def insert_ticker_entry(
        self,
        timestamp: datetime,
        bidPrice: float,
        askPrice: float,
        symbol: str = "BTC-USD",
    ) -> None:
        try:
            db = self.client[self.database_name]
            ticker_collection = db["ticker"]
            ticker_collection.insert_one(
                {
                    "time": timestamp,
                    "symbol": symbol,
                    "bid": Decimal128(bidPrice),
                    "ask": Decimal128(askPrice)
                }
            )
        except Exception as e:
            print(e)

    def indicator_signal_already_emitted(self, timestamp: datetime, indicator: str) -> bool:
        db = self.client[self.database_name]
        ta_signals = db["technicalAnalysisSignals"]
        count = ta_signals.count_documents({"referenceTime": timestamp, "indicator": indicator})        
        return count > 0
    
    def order_signal_exists(self, signal: OrderSignal, reference_time: datetime) -> bool:
        db = self.client[self.database_name]
        ta_signals = db["orderSignal"]
        count = ta_signals.count_documents({"referenceTime": reference_time, "type": signal.name})        
        return count > 0        
    
    def insert_order_signal(
        self,
        timestamp: datetime,
        referenceTimestamp: datetime,
        signal: OrderSignal,
        price: float
    ) -> None:
        try:
            db = self.client[self.database_name]
            ta_signals = db["orderSignal"]
            ta_signals.insert_one(
                {
                    "time": timestamp,
                    "referenceTime": referenceTimestamp,
                    "type": signal.name,
                    "price": price
                }
            )
        except Exception as e:
            print(e)



    def insert_ta_signal(
        self,
        timestamp: datetime,
        referenceTimestamp: datetime,
        indicator: str,
        detail: str,
    ) -> None:
        try:
            db = self.client[self.database_name]
            ta_signals = db["technicalAnalysisSignals"]
            ta_signals.insert_one(
                {
                    "time": timestamp,
                    "referenceTime": referenceTimestamp,
                    "indicator": indicator,
                    "detail": detail
                }
            )
        except Exception as e:
            print(e)

    def run_aggregation(self, pipeline: list, collection_name: str) -> list:
        try:
            db = self.client[self.database_name]
            ticker_collection = db[collection_name]
            return list(ticker_collection.aggregate(pipeline))
                
        except Exception as e:
            logging.error(e)
            return None     
