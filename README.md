# Crypto Arbitrage Detector

This project is a cryptocurrency arbitrage detection system that fetches data from exchanges, performs backtesting, and identifies potential arbitrage opportunities.

## Project Structure

The project consists of the following main components:

1. `data_fetching.py`: Handles fetching cryptocurrency data from various exchanges.
   - Connects to exchange APIs (Binance, Coinbase Pro, Kraken, Bitfinex)
   - Fetches real-time price data for specified cryptocurrency pairs
   - Handles API rate limiting and error handling
   - Normalizes data from different exchanges into a common format

2. `backtesting.py`: Implements backtesting functionality to evaluate trading strategies.
   - Loads historical price data
   - Simulates the arbitrage strategy over a specified time period
   - Calculates performance metrics (e.g., profit, win rate, Sharpe ratio)
   - Visualizes backtesting results using matplotlib

3. `arbitrage_detector.py`: Contains the logic for detecting arbitrage opportunities.
   - Compares prices across different exchanges
   - Calculates potential profit considering fees and slippage
   - Filters opportunities based on minimum profit threshold
   - Ranks opportunities based on profitability

4. `config.py`: Stores configuration settings for the project.
   - Lists supported exchanges and cryptocurrency pairs
   - Defines API endpoints for each exchange
   - Sets minimum profit threshold for arbitrage opportunities
   - Specifies backtesting parameters (time range, interval)
   - Contains other global settings used across the project

5. `main.py`: The entry point of the application, orchestrating the overall flow.
   - Initializes necessary components
   - Runs the main loop to continuously fetch data and detect arbitrage opportunities
   - Handles user input for starting/stopping the detector
   - Outputs results to the console or logs

## Arbitrage Detection Algorithm

The arbitrage detection algorithm works as follows:

1. Fetches real-time price data from supported exchanges for specified cryptocurrency pairs.
2. Calculates the price differences between exchanges for each pair.
3. Identifies potential arbitrage opportunities when the price difference exceeds a certain threshold.
4. Considers transaction fees and minimum order sizes to ensure the opportunity is profitable.
5. Outputs detected arbitrage opportunities with relevant details (exchanges, prices, potential profit).

## Supported Exchanges

Currently, the project supports the following exchanges:

- Binance
- Coinbase Pro
- Kraken
- Bitfinex

To add support for more exchanges, modify the `data_fetching.py` file and update the configuration in `config.py`.

## Environment and Dependencies

This project uses Poetry for dependency management. The required Python version and dependencies are specified in the `pyproject.toml` file.

### Python Version
- Python 3.8 or higher

### Main Dependencies
- requests: For making HTTP requests to exchange APIs
- pandas: For data manipulation and analysis
- numpy: For numerical computations
- matplotlib: For data visualization of backtesting results

To install the dependencies, make sure you have Poetry installed and run:
