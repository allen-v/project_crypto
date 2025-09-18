import ccxt.async_support as ccxt
import logging
import asyncio
from app.ingest_ws.rate_limit_checker import get_rate_limits
import time

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    def __init__(self, exchanges):
        self.exchanges = {name: getattr(ccxt, exchange_class.__name__)({'enableRateLimit': True}) for name, exchange_class in exchanges.items()}
        self.rate_limits = {}
        self.update_rate_limits()

    def update_rate_limits(self):
        rate_limit_data = get_rate_limits()
        for exchange, data in rate_limit_data.items():
            self.rate_limits[exchange] = max(1, int(data['requests_per_second']))
        logger.info(f"Updated rate limits: {self.rate_limits}")

    async def fetch_ticker_async(self, exchange_name, symbol):
        try:
            exchange = self.exchanges[exchange_name]
            logger.info(f"Fetching {symbol} from {exchange_name}")
            
            await exchange.load_markets()
            ticker = await exchange.fetch_ticker(symbol)
            
            processed_data = {
                'exchange': exchange_name,
                'symbol': symbol,
                'timestamp': ticker['timestamp'] or int(time.time() * 1000),
            }

            # Dynamically add all available fields from the ticker
            for key, value in ticker.items():
                if key not in processed_data:
                    processed_data[key] = value

            logger.info(f"Processed data for {symbol} from {exchange_name}: {processed_data}")
            return processed_data
        except Exception as e:
            logger.error(f"Error fetching {symbol} from {exchange_name}: {str(e)}")
            return None

    async def fetch_all_tickers_async(self):
        self.update_rate_limits()
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
        for exchange in self.exchanges.values():
            await exchange.close()

    def fetch_all_tickers(self):
        async def run():
            try:
                return await self.fetch_all_tickers_async()
            finally:
                await self.close_exchanges()

        return asyncio.run(run())

    def get_min_rate_limit(self):
        return min(self.rate_limits.values()) if self.rate_limits else 1

# Example usage
if __name__ == "__main__":
    # Define the exchanges
    exchanges = {
        'kraken': ccxt.kraken,
        'coinbase': ccxt.coinbase,
        'bitflyer': ccxt.bitflyer,
        'gemini': ccxt.gemini,
        'bitstamp': ccxt.bitstamp
    }

    # Initialize the DataFetcher
    fetcher = DataFetcher(exchanges)

    # Run the fetch_all_tickers function and display the output
    result = fetcher.fetch_all_tickers()
    print("All tickers fetched:")
    print(result)