import datetime
from signals import OrderSignal, TrendSignal, Signal
from mongoservice import MongoService
from ta_aggregations import macd_pipeline, rsi_pipeline


class TechnicalAnalysisService:
    def __init__(self, mongo_service: MongoService) -> None:
        self.mongo_service = mongo_service

    def signal_exists(self, order_signal: OrderSignal, reference_time: datetime) -> bool:
        return self.mongo_service.order_signal_exists(order_signal, reference_time)

    def insert_signal(self, current_time, time_before, order_signal: OrderSignal, price: float) -> bool:           
        self.mongo_service.insert_order_signal(
            timestamp=current_time,
            referenceTimestamp=time_before,
            signal=order_signal,
            price=price)

    def analyze_macd(self) -> tuple[Signal, float, float]:

        """ Calculates the MACD and returns a potential MACD signal and the corresponding signal and macd value"""

        macd_metrics = self.mongo_service.run_aggregation(macd_pipeline, 'ticker')
        if macd_metrics and len(macd_metrics) == 2:

            macd_before =  macd_metrics[1]['macdLine'].to_decimal()
            macd_now = macd_metrics[0]['macdLine'].to_decimal()
            signal_before = macd_metrics[1]['macdSignal'].to_decimal()
            signal_now = macd_metrics[0]['macdSignal'].to_decimal()

            time_before = macd_metrics[1]['_id']['time']
            #current_time = macd_metrics[0]['_id']['time'],
            before_below = macd_before < signal_before
            now_below = macd_now < signal_now

            trend = None

            if before_below and not now_below:
                trend = TrendSignal.MACD_BULLISH_CROSSOVER
            elif not before_below and now_below:
                trend = TrendSignal.MACD_BEARISH_CROSSOVER

            return Signal(trend, time_before) if trend else None, float(signal_now), float(macd_now)
            
    def analyze_rsi(self) -> tuple[Signal, float]:

        """ Calculates the RSI and returns a potential RSI signal and the corresponding RSI value
            returns the RSI signal (if applicable), the RSI value and the reference timestamp
        """

        rsi_metrics = self.mongo_service.run_aggregation(rsi_pipeline, 'ticker')
        if rsi_metrics and len(rsi_metrics) == 2:
            rsi = rsi_metrics[0]['rsi'].to_decimal()
            time_before = rsi_metrics[1]['time']
            #current_time = rsi_metrics[0]['time']
            
            trend = None
            
            if rsi <= 30:
                trend = TrendSignal.RSI_OVERSOLD
            elif rsi >= 70:
                trend = TrendSignal.RSI_OVERBOUGHT        
            
            return Signal(trend, time_before) if trend else None, float(rsi)