from enum import Enum
from signals import OrderSignal, TrendSignal

class TradeStrategy(Enum):
    MACD = 0
    RSI = 1
    MACD_RSI = 2

class BuySellStrategy:

    @staticmethod
    def macd_decision(macd: TrendSignal) -> OrderSignal:
        if macd:
            if macd == TrendSignal.MACD_BULLISH_CROSSOVER:
                return OrderSignal.BUY
            elif macd == TrendSignal.MACD_BEARISH_CROSSOVER:
                return OrderSignal.SELL
        
    @staticmethod
    def rsi_decision(rsi: TrendSignal) -> OrderSignal:  
        if rsi:
            if rsi == TrendSignal.RSI_OVERSOLD:
                return OrderSignal.BUY
            elif rsi == TrendSignal.RSI_OVERBOUGHT:
                return OrderSignal.SELL

    @staticmethod
    def macd_rsi_decision(macd: TrendSignal, rsi: TrendSignal) -> OrderSignal:  
        if rsi and macd:
            # Check if the MACD is bullish.
            if macd == TrendSignal.MACD_BULLISH_CROSSOVER:
                # Check if the RSI is oversold.
                if rsi == TrendSignal.RSI_OVERSOLD:
                # Buy the asset.
                    return OrderSignal.BUY
            elif macd == TrendSignal.MACD_BEARISH_CROSSOVER:
                # Check if the RSI is overbought.
                if rsi == TrendSignal.RSI_OVERBOUGHT:
                # Sell the asset.
                    return OrderSignal.SELL