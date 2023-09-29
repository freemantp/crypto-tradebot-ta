import datetime
from enum import Enum

class TrendSignal(Enum):
    MACD_BULLISH_CROSSOVER = 0
    MACD_BEARISH_CROSSOVER = 1
    RSI_OVERBOUGHT = 2,
    RSI_OVERSOLD = 3

class OrderSignal(Enum):
    BUY = 0,
    SELL = 1

class Signal:
    def __init__(self, signal: Enum, timestamp: datetime) -> None:
        self.signal = signal
        self.timestamp = timestamp
    def __str__(self):
        return f'Signal(name={self.signal.name}, timestamp={self.timestamp})'
