import logging
import argparse
from binance import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# Configure logging
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """Initialize the Binance client for Testnet or production."""
        self.client = Client(api_key, api_secret, testnet=testnet)
        logging.info("Initialized Binance client in testnet mode: %s", testnet)

    def validate_symbol(self, symbol):
        """Validate trading pair symbol."""
        try:
            info = self.client.get_symbol_info(symbol)
            if info:
                logging.info("Valid symbol: %s", symbol)
                return True
            logging.error("Invalid symbol: %s", symbol)
            return False
        except BinanceAPIException as e:
            logging.error("Error validating symbol %s: %s", symbol, str(e))
            return False

    def place_market_order(self, symbol, side, quantity):
        """Place a market order."""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info("Market order placed: %s", order)
            return order
        except BinanceAPIException as e:
            logging.error("Error placing market order: %s", str(e))
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order."""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info("Limit order placed: %s", order)
            return order
        except BinanceAPIException as e:
            logging.error("Error placing limit order: %s", str(e))
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        """Place a stop-limit order (Bonus feature)."""
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP_LOSS_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price
            )
            logging.info("Stop-limit order placed: %s", order)
            return order
        except BinanceAPIException as e:
            logging.error("Error placing stop-limit order: %s", str(e))
            return None

    def get_order_status(self, symbol, order_id):
        """Check the status of an order."""
        try:
            status = self.client.get_order(symbol=symbol, orderId=order_id)
            logging.info("Order status: %s", status)
            return status
        except BinanceAPIException as e:
            logging.error("Error fetching order status: %s", str(e))
            return None

def cli_interface():
    """Command-line interface to interact with the trading bot."""
    parser = argparse.ArgumentParser(description="Simplified Trading Bot for Binance Futures Testnet")
    parser.add_argument('--api-key', required=True, help="Binance API Key")
    parser.add_argument('--api-secret', required=True, help="Binance API Secret")
    parser.add_argument('--symbol', default="BTCUSDT", help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument('--order-type', choices=['market', 'limit', 'stop-limit'], default='market', help="Order type")
    parser.add_argument('--side', choices=['BUY', 'SELL'], required=True, help="Order side")
    parser.add_argument('--quantity', type=float, required=True, help="Order quantity")
    parser.add_argument('--price', type=float, help="Price for limit/stop-limit orders")
    parser.add_argument('--stop-price', type=float, help="Stop price for stop-limit orders")

    args = parser.parse_args()

    # Initialize bot
    bot = BasicBot(args.api_key, args.api_secret, testnet=True)

    # Validate symbol
    if not bot.validate_symbol(args.symbol):
        print(f"Invalid symbol: {args.symbol}")
        return

    # Place order based on type
    order = None
    if args.order_type == 'market':
        order = bot.place_market_order(args.symbol, args.side, args.quantity)
    elif args.order_type == 'limit':
        if not args.price:
            print("Price is required for limit orders")
            return
        order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
    elif args.order_type == 'stop-limit':
        if not args.price or not args.stop_price:
            print("Both price and stop-price are required for stop-limit orders")
            return
        order = bot.place_stop_limit_order(args.symbol, args.side, args.quantity, args.stop_price, args.price)

    # Output order details
    if order:
        print("Order placed successfully:")
        print(order)
        status = bot.get_order_status(args.symbol, order['orderId'])
        print("Order status:", status)
    else:
        print("Failed to place order. Check logs for details.")

if __name__ == "__main__":
    cli_interface()