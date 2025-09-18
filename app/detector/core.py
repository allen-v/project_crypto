import logging
from decimal import Decimal, getcontext
import networkx as nx
import pandas as pd

# Set decimal precision high enough for financial calculations
getcontext().prec = 28

logger = logging.getLogger(__name__)

class ArbitrageDetector:
    def __init__(self, min_profit_threshold=0.01, fees=None):
        self.min_profit_threshold = Decimal(str(min_profit_threshold))
        self.fees = fees or {}
        self.trading_pairs = set()

    def detect_triangular_arbitrage(self, data):
        opportunities = []
        self.trading_pairs = set(data['symbol'])
        currency_graph = self._build_currency_graph(self.trading_pairs)

        exchanges = data['exchange'].unique()
        for exchange in exchanges:
            try:
                exchange_data = data[data['exchange'] == exchange]
                G = self._build_exchange_graph(exchange_data)

                cycles = nx.simple_cycles(G)
                for cycle in cycles:
                    if len(cycle) == 3:
                        profit = self._calculate_profit(exchange_data, cycle, exchange)
                        if profit > self.min_profit_threshold:
                            opportunities.append({
                                'exchange': exchange,
                                'path': ' -> '.join(cycle),
                                'profit': float(profit)
                            })

            except Exception as e:
                logger.warning(f"Error in arbitrage calculation for {exchange}: {e}")

        return opportunities

    def _build_currency_graph(self, trading_pairs):
        G = nx.DiGraph()
        for pair in trading_pairs:
            base, quote = pair.split('/')
            G.add_edge(base, quote, pair=pair)
            G.add_edge(quote, base, pair=f"{quote}/{base}")
        return G

    def _build_exchange_graph(self, exchange_data):
        G = nx.DiGraph()
        for _, row in exchange_data.iterrows():
            symbol = row['symbol']
            base, quote = symbol.split('/')
            G.add_edge(base, quote, pair=symbol)
            G.add_edge(quote, base, pair=f"{quote}/{base}")
        return G

    def _calculate_profit(self, data, cycle, exchange):
        try:
            amount = Decimal('1')
            fee_structure = self.fees.get(exchange, {})
            for i in range(len(cycle)):
                base = cycle[i]
                quote = cycle[(i + 1) % len(cycle)]
                pair = f"{base}/{quote}"
                is_selling = True

                rate, volume = self._get_rate_and_volume(data, pair, is_selling)
                if rate is None or volume is None:
                    return Decimal('-1')

                max_trade_volume = min(amount, volume)
                if max_trade_volume == 0:
                    return Decimal('-1')

                pair_fees = fee_structure.get(pair, fee_structure.get('default', {}))
                fee = pair_fees.get('taker', Decimal('0'))  # Assume taker fee for worst-case scenario

                amount = max_trade_volume * rate * (Decimal('1') - fee)

            profit = amount - Decimal('1')
            return profit
        except Exception as e:
            logger.warning(f"Error calculating profit for {exchange} {' -> '.join(cycle)}: {e}")
            return Decimal('-1')

    def _get_rate_and_volume(self, data, pair, is_selling):
        row = data[data['symbol'] == pair]
        if row.empty:
            return None, None
        row = row.iloc[0]

        if is_selling:
            rate = Decimal(str(row['best_bid_price'])) if row['best_bid_price'] is not None else Decimal(str(row['bid']))
            volume = Decimal(str(row['best_bid_amount'])) if row['best_bid_amount'] is not None else Decimal(str(row['baseVolume']))
        else:
            rate = Decimal('1') / (Decimal(str(row['best_ask_price'])) if row['best_ask_price'] is not None else Decimal(str(row['ask'])))
            volume = Decimal(str(row['best_ask_amount'])) if row['best_ask_amount'] is not None else Decimal(str(row['quoteVolume']))

        if not self._is_valid_price(rate) or volume <= 0:
            logger.warning(f"Invalid price or volume for {pair}: rate={rate}, volume={volume}")
            return None, None

        return rate, volume

    def _is_valid_price(self, price):
        try:
            price = Decimal(str(price))
            return price > 0 and price != Decimal('Infinity')
        except (ValueError, TypeError, ArithmeticError):
            return False

    def detect_cross_exchange_arbitrage(self, data):
        opportunities = []
        for pair in self.trading_pairs:
            pair_data = data[data['symbol'] == pair]
            if len(pair_data) < 2:
                continue

            best_bid = pair_data.loc[pair_data['best_bid_price'].idxmax()]
            best_ask = pair_data.loc[pair_data['best_ask_price'].idxmin()]

            if best_bid['exchange'] != best_ask['exchange']:
                sell_fee = self.fees.get(best_bid['exchange'], {}).get(pair, {}).get('taker', Decimal('0'))
                buy_fee = self.fees.get(best_ask['exchange'], {}).get(pair, {}).get('taker', Decimal('0'))

                profit = (Decimal(str(best_bid['best_bid_price'])) * (Decimal('1') - sell_fee) /
                          (Decimal(str(best_ask['best_ask_price'])) * (Decimal('1') + buy_fee))) - Decimal('1')

                if profit > self.min_profit_threshold:
                    opportunities.append({
                        'pair': pair,
                        'buy_exchange': best_ask['exchange'],
                        'sell_exchange': best_bid['exchange'],
                        'profit': float(profit),
                        'volume': min(float(best_ask['best_ask_amount']), float(best_bid['best_bid_amount']))
                    })

        return opportunities

    def display_opportunities(self, opportunities, output_format='console'):
        if not opportunities:
            logger.info("No arbitrage opportunities found.")
            return

        if output_format == 'console':
            logger.info("Arbitrage Opportunities:")
            for opp in opportunities:
                if 'path' in opp:
                    logger.info(f"Triangular: Exchange: {opp['exchange']}, Path: {opp['path']}, "
                                f"Profit: {opp['profit']:.2%}")
                else:
                    logger.info(f"Cross-Exchange: Pair: {opp['pair']}, Buy: {opp['buy_exchange']}, "
                                f"Sell: {opp['sell_exchange']}, Profit: {opp['profit']:.2%}, "
                                f"Volume: {opp['volume']:.8f}")
        elif output_format == 'json':
            import json
            print(json.dumps(opportunities, indent=2))
        elif output_format == 'dataframe':
            df = pd.DataFrame(opportunities)
            print(df)
            return df
        else:
            logger.error(f"Unsupported output format: {output_format}")