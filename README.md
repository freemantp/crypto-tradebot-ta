# Crypto-currency tradebot

A serverless crypto trading bot that uses technical analysis to generate buy/sell signals and exectute trades on the Lykke echange

 ***HINT:*** Lykke went out of business early 2025, the repository is onyl for demonstrational purpose

 **DISCLAIMER**: Crypto markets are highly volatile, and using trade bot can cause total loss. Use at your own risk

## Overview

The trade bot is built as a set of AWS Lambda functions that interact with the Lykke Exchange API to:

1. Ingest cryptocurrency price data from Lykke Exchange
2. Apply technical analysis algorithms (MACD, RSI) to generate buy/sell signals
3. Execute trades on the exchange based on signals

## Architecture
<img width="640" alt="tabot-arch" src="https://github.com/user-attachments/assets/3c3fa317-3da4-4af6-963f-4864091a828a" />

The system consists of three main components:

### 1. Ticker Ingestor
- Fetches current price data from Lykke Exchange
- Stores data in MongoDB
- Calculates technical indicators (MACD, RSI)
- Generates buy/sell signals based on indicator thresholds
- Notifies the order executor via SNS when a trading opportunity is identified

### 2. Order Executor
- Listens for buy/sell signals from the ticker ingestor
- Checks account balances on the Lykke Exchange
- Executes market orders when there's sufficient balance
- Can operate in simulation mode for testing without placing real orders

### 3. Portfolio Management
- Displays transaction history
- Monitors account balances

## Technologies Used

- Python 3.11+
- AWS Lambda for serverless computing
- MongoDB Atlas for price data storage
- Amazon SNS for notifications between components
- gRPC for Lykke Exchange API communication
- Protobuf for data serialization

## Trading Strategies

The bot currently supports three trading strategies:

1. **MACD Strategy**: Generates buy signals on bullish crossovers and sell signals on bearish crossovers
2. **RSI Strategy**: Generates buy signals when RSI is oversold (<30) and sell signals when RSI is overbought (>70)
3. **MACD-RSI Combined Strategy**: Generates signals only when both indicators agree (e.g., buy when MACD shows bullish crossover AND RSI is oversold)

## Setup and Configuration

### Prerequisites
- Python 3.11+
- MongoDB DB (eg. through MongoDB Atlas)
- Lykke Exchange API token
- AWS account with Lambda, SNS permissions

### Environment Variables
The following environment variables must be set:

```
LYKKE_HFT_TOKEN=your_lykke_api_token
MONGO_HOST=your_mongodb_host
MONGO_CREDENTIALS=your_mongodb_credentials
TRADES_SIMULATED=true/false
ORDER_SNS_TOPIC=your_sns_topic_arn
```

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Deploy lambda functions to your AWS environment
