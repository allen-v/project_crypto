import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import asyncio
import ccxt
import logging

# Import your project modules
from data_fetching import DataFetcher
from data_processing import DataProcessor
from arbitrage_detector import ArbitrageDetector
from exchange_setup import ExchangeSetup
import config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit app
st.set_page_config(page_title="Crypto Arbitrage Detector", layout="wide")

st.title("Cryptocurrency Arbitrage Detection System")

async def main():
    data_fetcher = None
    try:
        # Initialize components
        exchange_setup = ExchangeSetup()
        exchanges = exchange_setup.get_exchanges()
        for exchange in exchanges.values():
            exchange.options['maxRetriesOnFailure'] = 3
            exchange.options['maxRetriesOnFailureDelay'] = 1000
        st.write(f"Exchanges: {list(exchanges.keys())}")
        data_fetcher = DataFetcher(exchanges)
        data_processor = DataProcessor(config.DB_NAME)
        arbitrage_detector = ArbitrageDetector(min_profit_threshold=config.MIN_PROFIT_THRESHOLD, fees=config.EXCHANGE_FEES)

        st.success("Components initialized successfully")

        # Sidebar
        st.sidebar.header("Controls")
        selected_exchange = st.sidebar.selectbox("Select Exchange", list(exchanges.keys()))
        refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 
                                             min_value=10, max_value=300, value=60)

        # Main content
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Real-time Market Data")
            
            @st.cache_data(ttl=refresh_interval)
            def fetch_latest_data():
                try:
                    logger.info("Starting to fetch latest data...")
                    loop = asyncio.get_event_loop()
                    data = loop.run_until_complete(data_fetcher.fetch_all_tickers_async())
                    logger.info("Data fetched successfully")
                    return data
                except Exception as e:
                    logger.error(f"Error when fetching data: {str(e)}")
                    st.error(f"Error when fetching data: {str(e)}")
                    return None

            latest_data = fetch_latest_data()
            if latest_data:
                st.write("Raw data fetched:")
                st.write(latest_data)
                try:
                    df = pd.DataFrame(latest_data)
                    st.dataframe(df)
                except Exception as e:
                    logger.error(f"Error creating DataFrame: {str(e)}")
                    st.error(f"Error creating DataFrame: {str(e)}")
            else:
                st.warning("No data available. Please check your connection.")

        with col2:
            st.subheader("Arbitrage Opportunities")
            
            def detect_arbitrage():
                if latest_data is None:
                    logger.warning("No data available for arbitrage detection")
                    return None, None
                try:
                    logger.info("Detecting arbitrage opportunities...")
                    table = data_processor.process_ticker_data(latest_data)
                    triangular = arbitrage_detector.detect_triangular_arbitrage(table)
                    cross_exchange = arbitrage_detector.detect_cross_exchange_arbitrage(table)
                    logger.info("Arbitrage detection completed")
                    return triangular, cross_exchange
                except Exception as e:
                    logger.error(f"Error detecting arbitrage: {str(e)}")
                    st.error(f"Error detecting arbitrage: {str(e)}")
                    return None, None

            triangular_opps, cross_exchange_opps = detect_arbitrage()
            
            st.write("Triangular Arbitrage:")
            if triangular_opps:
                st.table(pd.DataFrame(triangular_opps))
            else:
                st.info("No triangular arbitrage opportunities detected.")
            
            st.write("Cross-Exchange Arbitrage:")
            if cross_exchange_opps:
                st.table(pd.DataFrame(cross_exchange_opps))
            else:
                st.info("No cross-exchange arbitrage opportunities detected.")

        # Historical Data Visualization
        st.subheader("Historical Data Visualization")
        days_ago = st.slider("Select timeframe", 1, 30, 7)
        start_date = datetime.now() - timedelta(days=days_ago)
        end_date = datetime.now()

        try:
            logger.info("Fetching historical data...")
            historical_data = data_processor.get_historical_data(None, start_date, end_date)
            logger.info("Historical data fetched successfully")

            if not historical_data.empty:
                fig = go.Figure()
                for symbol in historical_data['symbol'].unique():
                    symbol_data = historical_data[historical_data['symbol'] == symbol]
                    fig.add_trace(go.Scatter(x=symbol_data['timestamp'], y=symbol_data['last'],
                                             mode='lines', name=symbol))
                fig.update_layout(title="Price History", xaxis_title="Date", yaxis_title="Price")
                st.plotly_chart(fig)
            else:
                st.warning("No historical data available for the selected timeframe.")
        except Exception as e:
            logger.error(f"Error fetching historical data: {str(e)}")
            st.error(f"Error fetching historical data: {str(e)}")

        # System Information
        st.subheader("System Information")
        st.json({
            "Supported Exchanges": list(exchanges.keys()),
            "Minimum Profit Threshold": f"{config.MIN_PROFIT_THRESHOLD:.2%}",
            "Database": config.DB_NAME,
            "Refresh Interval": f"{refresh_interval} seconds"
        })

        # Footer
        st.markdown("---")
        st.markdown("Cryptocurrency Arbitrage Detection System - Developed with Streamlit")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

    finally:
        # Close all exchange connections
        if data_fetcher:
            await data_fetcher.close_exchanges()

if __name__ == "__main__":
    asyncio.run(main())
