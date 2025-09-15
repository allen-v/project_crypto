import ibis
import duckdb
import logging
from datetime import datetime
import time
import random

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = None
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.con = duckdb.connect(self.db_path)
            ibis.set_backend('duckdb')
            self.db = ibis.duckdb.connect(self.db_path)
            logger.info(f"Connected to database: {self.db_path}")
        except duckdb.IOException as e:
            logger.error(f"Error connecting to database: {str(e)}")
            raise

    def process_ticker_data(self, ticker_data):
        """Process ticker data into a DuckDB table with retry mechanism."""
        if ticker_data is None or len(ticker_data) == 0:
            logger.warning("No ticker data to process")
            return None

        table_name = 'ticker_data'
        max_retries = 5
        base_delay = 1  # in seconds

        for attempt in range(max_retries):
            try:
                # Determine columns dynamically
                columns = set()
                for item in ticker_data:
                    columns.update(item.keys())
                columns = list(columns)

                # Create table if it doesn't exist
                column_definitions = ', '.join([f"{col} {'BIGINT' if col == 'timestamp' else 'DOUBLE' if col in ['bid', 'ask', 'last', 'high', 'low', 'baseVolume', 'quoteVolume'] else 'VARCHAR'}" for col in columns])
                self.con.execute(f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        {column_definitions}
                    )
                """)
                
                # Filter out entries with null values in critical fields
                valid_data = [
                    item for item in ticker_data
                    if all(item.get(field) is not None for field in ['symbol', 'bid', 'ask', 'timestamp'])
                ]
                
                if not valid_data:
                    logger.warning("No valid data to insert after filtering")
                    return None

                # Prepare the data for insertion
                data_to_insert = [
                    tuple(item.get(col) for col in columns)
                    for item in valid_data
                ]
                
                # Insert the data
                placeholders = ', '.join(['?' for _ in columns])
                self.con.executemany(f"""
                    INSERT INTO {table_name} ({', '.join(columns)})
                    VALUES ({placeholders})
                """, data_to_insert)
                
                logger.info(f"Processed {len(data_to_insert)} valid ticker entries")
                return self.db.table(table_name)

            except duckdb.IOException as e:
                if "Conflicting lock is held" in str(e):
                    delay = (base_delay * 2 ** attempt) + (random.randint(0, 1000) / 1000)
                    logger.warning(f"Database lock error. Retrying in {delay:.2f} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(delay)
                    self.close()  # Close the current connection
                    self.connect()  # Reconnect to the database
                else:
                    logger.error(f"Unexpected IO error: {e}")
                    raise
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                raise

        logger.error(f"Failed to process ticker data after {max_retries} attempts")
        raise Exception("Max retries exceeded for processing ticker data")

    def get_historical_data(self, symbol, start_date, end_date):
        """Retrieve historical data for a given symbol and date range."""
        try:
            start_timestamp = int(start_date.timestamp() * 1000)
            end_timestamp = int(end_date.timestamp() * 1000)
            query = self.db.table('ticker_data').filter(
                (ibis._.timestamp >= start_timestamp) &
                (ibis._.timestamp <= end_timestamp)
            )
            if symbol:
                query = query.filter(ibis._.symbol == symbol)
            return query.execute()
        except Exception as e:
            logger.error(f"Error retrieving historical data: {str(e)}")
            raise

    def display_ticker_data(self, table):
        """Display the ticker data summary."""
        summary = table.group_by('exchange').aggregate([
            table.bid.mean().name('avg_bid'),
            table.ask.mean().name('avg_ask'),
            table.last.mean().name('avg_last'),
            table.baseVolume.sum().name('total_base_volume'),
            table.quoteVolume.sum().name('total_quote_volume')
        ]).execute()
        logger.info("Ticker Data Summary:")
        logger.info(summary)

    def save_ticker_data(self, table, filename=None):
        """Save the ticker data to a CSV file."""
        if filename is None:
            filename = f'ticker_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        table.execute().to_csv(filename, index=False)
        logger.info(f"Data saved to {filename}")

    def close(self):
        """Close the database connection."""
        if self.con:
            self.con.close()
            self.con = None
        if self.db:
            self.db.close()
            self.db = None
        logger.info("Database connection closed.")