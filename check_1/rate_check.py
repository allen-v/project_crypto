import ccxt
from dotenv import load_dotenv
import time
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# List of exchanges to set up
exchanges = {
    "coinbase": ccxt.coinbase,
    "bitflyer": ccxt.bitflyer,
    "gemini": ccxt.gemini,
    "kraken": ccxt.kraken,
    "bitstamp": ccxt.bitstamp
}

def get_rate_limits():
    """Fetch rate limit information from exchanges."""
    rate_limit_data = {}
    for exchange_name, exchange_class in exchanges.items():
        exchange = exchange_class()
        rate_limit = exchange.rateLimit
        rate_limit_seconds = rate_limit / 1000
        requests_per_second = 1000 / rate_limit if rate_limit > 0 else float('inf')
        rate_limit_data[exchange_name] = {
            "rate_limit_ms": rate_limit,
            "rate_limit_s": rate_limit_seconds,
            "requests_per_second": requests_per_second
        }
    return rate_limit_data

def print_rate_limits(rate_limit_data):
    """Print rate limits in a table format."""
    sorted_data = sorted(rate_limit_data.items(), key=lambda x: x[1]['rate_limit_ms'])
    max_lengths = {
        "Exchange": max(len("Exchange"), max(len(exchange) for exchange in rate_limit_data.keys())),
        "Rate Limit (ms)": max(len("Rate Limit (ms)"), max(len(str(data['rate_limit_ms'])) for data in rate_limit_data.values())),
        "Rate Limit (s)": max(len("Rate Limit (s)"), max(len(f"{data['rate_limit_s']:.3f}") for data in rate_limit_data.values())),
        "Requests per Second": max(len("Requests per Second"), max(len(f"{data['requests_per_second']:.2f}") for data in rate_limit_data.values())),
    }

    print(f"\nRate Limit Check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"| {'Exchange'.ljust(max_lengths['Exchange'])} | "
          f"{'Rate Limit (ms)'.ljust(max_lengths['Rate Limit (ms)'])} | "
          f"{'Rate Limit (s)'.ljust(max_lengths['Rate Limit (s)'])} | "
          f"{'Requests per Second'.ljust(max_lengths['Requests per Second'])} | "
          f"{'Rank (Fastest)'} |")
    print(f"|{'-' * (max_lengths['Exchange'] + 2)}|"
          f"{'-' * (max_lengths['Rate Limit (ms)'] + 2)}|"
          f"{'-' * (max_lengths['Rate Limit (s)'] + 2)}|"
          f"{'-' * (max_lengths['Requests per Second'] + 2)}|"
          f"{'-' * 17}|")

    for idx, (exchange, data) in enumerate(sorted_data):
        print(f"| {exchange.capitalize().ljust(max_lengths['Exchange'])} | "
              f"{str(data['rate_limit_ms']).ljust(max_lengths['Rate Limit (ms)'])} | "
              f"{f'{data['rate_limit_s']:.3f}'.ljust(max_lengths['Rate Limit (s)'])} | "
              f"{f'{data['requests_per_second']:.2f}'.ljust(max_lengths['Requests per Second'])} | "
              f"{idx + 1} |")

def main():
    """Main function to run the continuous rate limit checker."""
    print("Starting continuous rate limit checker. Press Ctrl+C to stop.")
    try:
        while True:
            rate_limits = get_rate_limits()
            print_rate_limits(rate_limits)
            time.sleep(60)  # Wait for 60 seconds before the next check
    except KeyboardInterrupt:
        print("\nStopping rate limit checker.")

if __name__ == "__main__":
    main()
