import ccxt.async_support as ccxt
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class ExchangeSetup:
    def __init__(self):
        self.exchanges = {}
        for exchange_name, exchange_class in [
            ("coinbase", ccxt.coinbase),
            ("bitflyer", ccxt.bitflyer),
            ("gemini", ccxt.gemini),
            ("kraken", ccxt.kraken),
            ("bitstamp", ccxt.bitstamp)
        ]:
            api_key = os.getenv(f"{exchange_name.upper()}_API_KEY")
            secret_key = os.getenv(f"{exchange_name.upper()}_SECRET")
            
            logger.debug(f"Setting up {exchange_name}")
            logger.debug(f"{exchange_name} API Key present: {bool(api_key)}")
            logger.debug(f"{exchange_name} Secret Key present: {bool(secret_key)}")
            
            if api_key and secret_key:
                secret_key = secret_key.replace("\\n", "\n")
                self.exchanges[exchange_name] = exchange_class({
                    'apiKey': api_key,
                    'secret': secret_key,
                    'enableRateLimit': True
                })
            else:
                logger.warning(f"Missing API credentials for {exchange_name}")

    def get_exchanges(self):
        """Return all initialized exchanges."""
        return self.exchanges