# Simplified Trading Bot for Binance Futures Testnet

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This project implements a **Python-based trading bot** for the **Binance Futures Testnet (USDT-M)**. The bot supports **market**, **limit**, and **stop-limit** (bonus feature) orders, with a command-line interface (CLI), comprehensive logging, and robust error handling.

## Features

- **Order Types**: Place **market**, **limit**, and **stop-limit** orders on Binance Futures Testnet.
- **Order Sides**: Supports both **BUY** and **SELL** sides.
- **API Integration**: Uses the official [python-binance](https://python-binance.readthedocs.io/) library to interact with the Binance API.
- **CLI Interface**: Accepts and validates user inputs via a command-line interface.
- **Logging**: Logs all API requests, responses, and errors to `logs/bot.log`.
- **Error Handling**: Robust handling of API errors and input validation.
- **Bonus Feature**: Implements **stop-limit** orders for advanced trading functionality.

## Project Structure

```
trading_bot/
├── trading_bot.py       # Main bot logic
├── requirements.txt     # Project dependencies
├── logs/               # Log files
│   └── bot.log
└── README.md           # Project documentation
```

## Prerequisites

- **Python 3.8+**: Ensure Python is installed ([download here](https://www.python.org/downloads/)).
- **Binance Futures Testnet Account**:
  - Register at [Binance Futures Testnet](https://testnet.binancefuture.com).
  - Generate an **API Key** and **API Secret** from the Testnet dashboard.
- **Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

## Setup Instructions

1. **Obtain the Project Files**:
   - Download or copy the project files to a local directory.
   - Navigate to the project directory:
     ```bash
     cd trading_bot
     ```
2. **Install Dependencies**:
   - Install the required Python library:
     ```bash
     pip install python-binance==1.0.19
     ```
3. **Configure Logging**:
   - Ensure the `logs/` directory exists. If not, create it:
     ```bash
     mkdir logs
     ```
4. **Obtain API Credentials**:
   - Log in to the [Binance Futures Testnet](https://testnet.binancefuture.com) and generate an API Key and Secret.
   - Keep these credentials secure and do not include them in shared files.

## Usage

Run the bot using the command-line interface with the following syntax:

```bash
python trading_bot.py --api-key <API_KEY> --api-secret <API_SECRET> --symbol <SYMBOL> --order-type <ORDER_TYPE> --side <SIDE> --quantity <QUANTITY> [--price <PRICE>] [--stop-price <STOP_PRICE>]
```

### Arguments

| Argument       | Description                                   | Required | Default      |
|----------------|-----------------------------------------------|----------|--------------|
| `--api-key`    | Binance API Key                              | Yes      | -            |
| `--api-secret` | Binance API Secret                           | Yes      | -            |
| `--symbol`     | Trading pair (e.g., `BTCUSDT`)               | No       | `BTCUSDT`    |
| `--order-type` | Order type (`market`, `limit`, `stop-limit`) | No       | `market`     |
| `--side`       | Order side (`BUY` or `SELL`)                 | Yes      | -            |
| `--quantity`   | Order quantity (e.g., `0.001`)               | Yes      | -            |
| `--price`      | Price for limit/stop-limit orders            | No       | -            |
| `--stop-price` | Stop price for stop-limit orders             | No       | -            |

### Examples

1. **Place a Market Order**:
   ```bash
   python trading_bot.py --api-key <your_api_key> --api-secret <your_api_secret> --symbol BTCUSDT --order-type market --
