"""
Configuration settings for the Cryptocurrency Arbitrage Detection System.
"""

from decimal import Decimal

# Database
DB_NAME = 'crypto_data_check_1.db'

# Arbitrage settings
MIN_PROFIT_THRESHOLD = Decimal('0.005')  # 0.5%

# Detailed fee structure
EXCHANGE_FEES = {
    'coinbase': {
        'default': {'maker': Decimal('0.005'), 'taker': Decimal('0.005')},
        'BTC/USD': {'maker': Decimal('0.0045'), 'taker': Decimal('0.0045')},
    },
    'bitflyer': {
        'default': {'maker': Decimal('0.001'), 'taker': Decimal('0.001')},
    },
    'gemini': {
        'default': {'maker': Decimal('0.0035'), 'taker': Decimal('0.0035')},
    },
    'kraken': {
        'default': {'maker': Decimal('0.0026'), 'taker': Decimal('0.0026')},
    },
    'bitstamp': {
        'default': {'maker': Decimal('0.005'), 'taker': Decimal('0.005')},
    }
}

# Time intervals
FETCH_INTERVAL = 300  # 5 minutes
RETRY_INTERVAL = 60  # 1 minute
DEFAULT_REFRESH_INTERVAL = 60  # 1 minute

# Backtesting
BACKTEST_START_DATE = '2024-01-01'
BACKTEST_END_DATE = '2024-08-17'

# Exchanges
SUPPORTED_EXCHANGES = ['coinbase', 'bitflyer', 'gemini', 'kraken', 'bitstamp']

# Logging
LOG_FILE = 'crypto_arbitrage.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'