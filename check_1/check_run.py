import asyncio
import logging
from typing import List, Dict, Any, Union
from check_1.fetch import fetch_all_tickers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting to fetch ticker data")
    try:
        tickers: List[Union[Dict[str, Any], BaseException]] = await fetch_all_tickers()
        valid_tickers = [t for t in tickers if isinstance(t, dict)]
        logger.info(f"Fetched {len(valid_tickers)} valid tickers out of {len(tickers)} total")
        
        for ticker in valid_tickers[:20]:  # Print first 20 valid tickers as a sample
            exchange = ticker.get('exchange', 'Unknown')
            symbol = ticker.get('symbol', 'Unknown')
            last = ticker.get('last', 'N/A')
            bid = ticker.get('bid', 'N/A')
            ask = ticker.get('ask', 'N/A')
            volume = ticker.get('baseVolume', 'N/A')
            
            print(f"{exchange} - {symbol}: Last: {last}, Bid: {bid}, Ask: {ask}, Volume: {volume}")
    
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
