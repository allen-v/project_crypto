import ccxt.async_support as ccxt
from dotenv import load_dotenv
import logging
import asyncio
import time
from check_1.rate_check import get_rate_limits  # Corrected import

# Load environment variables from .env file
load_dotenv()

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of exchanges to set up
exchanges = {
    "coinbase": ccxt.coinbase,
    "bitflyer": ccxt.bitflyer,
    "gemini": ccxt.gemini,
    "kraken": ccxt.kraken,
    "bitstamp": ccxt.bitstamp
}

class DataFetcher:
    def __init__(self):
        # Initialize exchanges with rate limiting enabled
        self.exchanges = {name: exchange_class({'enableRateLimit': True}) for name, exchange_class in exchanges.items()}
        self.rate_limits = {}
        self.semaphores = {}
        self.update_rate_limits()

    def update_rate_limits(self):
        """Fetch and update rate limits from exchanges."""
        rate_limit_data = get_rate_limits()
        for exchange_name, data in rate_limit_data.items():
            requests_per_second = data['requests_per_second'] or 1
            self.rate_limits[exchange_name] = max(1, int(requests_per_second))
            # Create semaphores to control the rate limit
            self.semaphores[exchange_name] = asyncio.Semaphore(int(requests_per_second))

        logger.info(f"Updated rate limits and semaphores: {self.rate_limits}")

    async def fetch_ticker_async(self, exchange_name, symbol):
        """Fetch ticker data for a specific symbol asynchronously."""
        try:
            exchange = self.exchanges[exchange_name]
            semaphore = self.semaphores[exchange_name]
            async with semaphore:
                await exchange.load_markets()
                ticker = await exchange.fetch_ticker(symbol)
                
                processed_data = self.process_ticker_data(exchange_name, symbol, ticker)
                logger.info(f"Processed data for {symbol} from {exchange_name}: {processed_data}")
                return processed_data
        except Exception as e:
            logger.error(f"Error fetching {symbol} from {exchange_name}: {str(e)}")
            return None

    def process_ticker_data(self, exchange_name, symbol, ticker):
        """Process and structure ticker data."""
        processed_data = {
            'exchange': exchange_name,
            'symbol': symbol,
            'timestamp': ticker.get('timestamp') or int(time.time() * 1000),
        }
        # Dynamically add all available fields from the ticker
        for key, value in ticker.items():
            if key not in processed_data:
                processed_data[key] = value

        return processed_data

    async def fetch_all_tickers_async(self):
        """Fetch all tickers asynchronously for all exchanges."""
        self.update_rate_limits()  # Ensure rate limits are up-to-date
        tasks = []
        for exchange_name, exchange in self.exchanges.items():
            await exchange.load_markets()
            for symbol in exchange.symbols:
                tasks.append(self.fetch_ticker_async(exchange_name, symbol))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        valid_results = [r for r in results if r is not None and not isinstance(r, Exception)]
        
        logger.info(f"Fetched {len(valid_results)} valid tickers")
        return valid_results

    async def close_exchanges(self):
        """Close connections to all exchanges."""
        for exchange in self.exchanges.values():
            await exchange.close()

    def fetch_all_tickers(self):
        """Run the asynchronous fetching function synchronously."""
        async def run():
            try:
                return await self.fetch_all_tickers_async()
            finally:
                await self.close_exchanges()

        return asyncio.run(run())

async def fetch_all_tickers():
    fetcher = DataFetcher()
    try:
        return await fetcher.fetch_all_tickers_async()
    finally:
        await fetcher.close_exchanges()

if __name__ == "__main__":
    # Initialize the DataFetcher
    fetcher = DataFetcher()

    # Fetch all tickers and display the output
    result = fetcher.fetch_all_tickers()
    print("All tickers fetched:")
    print(result)