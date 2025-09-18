"""
Cryptocurrency Arbitrage Detection System

This script runs a continuous process to detect arbitrage opportunities
across various cryptocurrency exchanges. It fetches data, processes it,
detects arbitrage opportunities, and performs backtesting while respecting
rate limits of each exchange.
"""

import asyncio
import logging
from datetime import datetime
from app.ingest_ws.exchange_setup import ExchangeSetup
from app.ingest_ws.data_fetching import DataFetcher
from app.ingest_ws.data_processing import DataProcessor
from app.detector.core import ArbitrageDetector
from app.config import settings as config
import streamlit as st

# Set up logging
handler = logging.StreamHandler()
formatter = logging.Formatter(config.LOG_FORMAT)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

async def fetch_and_process_data(data_fetcher, data_processor, arbitrage_detector):
    try:
        data_fetcher.update_rate_limits()
        
        ticker_data = await data_fetcher.fetch_all_tickers_async()

        if not ticker_data:
            logger.error("No ticker data was fetched. Check your internet connection and API access.")
            return False

        table = data_processor.process_ticker_data(ticker_data)
        data_processor.display_ticker_data(table)

        triangular_opportunities = arbitrage_detector.detect_triangular_arbitrage(table)
        cross_exchange_opportunities = arbitrage_detector.detect_cross_exchange_arbitrage(table)
        
        logger.info(f"Detected {len(triangular_opportunities)} triangular arbitrage opportunities")
        logger.info(f"Detected {len(cross_exchange_opportunities)} cross-exchange arbitrage opportunities")
        
        arbitrage_detector.display_opportunities(triangular_opportunities, output_format='console')
        arbitrage_detector.display_opportunities(cross_exchange_opportunities, output_format='console')

        # Update Streamlit session state
        if 'processed_data' in st.session_state:
            st.session_state.processed_data = table.execute()
            st.session_state.triangular_opportunities = triangular_opportunities
            st.session_state.cross_exchange_opportunities = cross_exchange_opportunities

        return True
    except Exception as e:
        logger.exception(f"Error in fetch_and_process_data: {str(e)}")
        return False

async def main_loop():
    logger.info("Starting Cryptocurrency Arbitrage Detection System")
    
    exchange_setup = ExchangeSetup()
    exchanges = exchange_setup.get_exchanges()
    
    logger.info(f"Exchanges set up: {list(exchanges.keys())}")

    if not exchanges:
        logger.error("No exchanges were successfully set up. Check your API credentials.")
        return

    data_fetcher = DataFetcher(exchanges)
    data_processor = DataProcessor(config.DB_NAME)
    arbitrage_detector = ArbitrageDetector(min_profit_threshold=config.MIN_PROFIT_THRESHOLD, fees=config.EXCHANGE_FEES)

    while True:
        success = await fetch_and_process_data(data_fetcher, data_processor, arbitrage_detector)
        
        if success:
            sleep_interval = 1 / data_fetcher.get_min_rate_limit()
            logger.info(f"Sleeping for {sleep_interval:.2f} seconds")
            await asyncio.sleep(sleep_interval)
        else:
            await asyncio.sleep(config.RETRY_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main_loop())