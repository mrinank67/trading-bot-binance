Simplified Trading Bot for Binance Futures Testnet
This project implements a Python-based trading bot for the Binance Futures Testnet (USDT-M) as part of the Junior Python Developer application task. The bot supports market, limit, and stop-limit (bonus feature) orders, with a command-line interface (CLI), comprehensive logging, and error handling.
Features

Order Types: Place market, limit, and stop-limit orders on Binance Futures Testnet.
Order Sides: Supports both BUY and SELL sides.
API Integration: Uses the official python-binance library to interact with the Binance API.
CLI Interface: Accepts and validates user inputs via a command-line interface.
Logging: Logs all API requests, responses, and errors to logs/bot.log.
Error Handling: Robust handling of API errors and input validation.
Bonus Feature: Implements stop-limit orders for advanced trading functionality.

Project Structure
trading_bot/
├── trading_bot.py       # Main bot logic
├── requirements.txt     # Project dependencies
├── logs/               # Log files
│   └── bot.log
└── README.md           # Project documentation

Prerequisites

Python 3.8+
Binance Futures Testnet Account:
Register at https://testnet.binancefuture.com.
Generate API Key and API Secret from the Testnet dashboard.


Dependencies:pip install -r requirements.txt



Setup Instructions

Clone the Repository:git clone <repository-url>
cd trading_bot


Install Dependencies:pip install python-binance


Configure Logging:
Ensure the logs/ directory exists. If not, create it:mkdir logs




Obtain API Credentials:
Log in to the Binance Futures Testnet and generate an API Key and Secret.
Keep these credentials secure and do not commit them to version control.



Usage
Run the bot using the command-line interface with the following syntax:
python trading_bot.py --api-key <API_KEY> --api-secret <API_SECRET> --symbol <SYMBOL> --order-type <ORDER_TYPE> --side <SIDE> --quantity <QUANTITY> [--price <PRICE>] [--stop-price <STOP_PRICE>]

Arguments

--api-key: Binance API Key (required).
--api-secret: Binance API Secret (required).
--symbol: Trading pair (e.g., BTCUSDT, default: BTCUSDT).
--order-type: Order type (market, limit, stop-limit, default: market).
--side: Order side (BUY or SELL, required).
--quantity: Order quantity (e.g., 0.001, required).
--price: Price for limit or stop-limit orders (optional).
--stop-price: Stop price for stop-limit orders (optional).

Examples

Place a Market Order:
python trading_bot.py --api-key <your_api_key> --api-secret <your_api_secret> --symbol BTCUSDT --order-type market --side BUY --quantity 0.001

Output: Order details and execution status.

Place a Limit Order:
python trading_bot.py --api-key <your_api_key> --api-secret <your_api_secret> --symbol BTCUSDT --order-type limit --side BUY --quantity 0.001 --price 60000

Output: Order details and execution status.

Place a Stop-Limit Order (Bonus Feature):
python trading_bot.py --api-key <your_api_key> --api-secret <your_api_secret> --symbol BTCUSDT --order-type stop-limit --side BUY --quantity 0.001 --price 60000 --stop-price 59000

Output: Order details and execution status.


Log Files

All API interactions and errors are logged to logs/bot.log.
Example log entry:2025-06-24 19:45:00,123 - INFO - Initialized Binance client in testnet mode: True
2025-06-24 19:45:01,456 - INFO - Valid symbol: BTCUSDT
2025-06-24 19:45:02,789 - INFO - Market order placed: {'orderId': 123456, 'symbol': 'BTCUSDT', ...}



Testing

Test the bot on the Binance Futures Testnet with small quantities (e.g., 0.001 BTCUSDT).
Verify that logs capture all API interactions and errors.
Ensure the CLI validates inputs (e.g., missing price for limit orders).

Notes

Security: Do not hardcode API credentials or commit them to GitHub.
Error Handling: The bot handles API errors and validates inputs. Check logs/bot.log for details on failures.
Extensibility: The code is structured for reusability, with potential to add more order types (e.g., OCO) or a graphical UI.
