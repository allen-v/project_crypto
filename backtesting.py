import pandas as pd
from arbitrage_detector import ArbitrageDetector

class Backtester:
    def __init__(self, data_processor, arbitrage_detector):
        self.data_processor = data_processor
        self.arbitrage_detector = arbitrage_detector

    def run_backtest(self, start_date, end_date):
        historical_data = self.data_processor.get_historical_data(None, start_date, end_date)
        triangular_opportunities = []
        cross_exchange_opportunities = []

        for timestamp in historical_data['timestamp'].unique():
            data_slice = historical_data[historical_data['timestamp'] == timestamp]
            table = self.data_processor.db.create_table('temp_table', data_slice)
            
            triangular_opp = self.arbitrage_detector.detect_triangular_arbitrage(table)
            cross_exchange_opp = self.arbitrage_detector.detect_cross_exchange_arbitrage(table)
            
            if triangular_opp:
                triangular_opportunities.extend(triangular_opp)
            if cross_exchange_opp:
                cross_exchange_opportunities.extend(cross_exchange_opp)
            
            self.data_processor.db.drop_table('temp_table')

        return {
            'triangular': triangular_opportunities,
            'cross_exchange': cross_exchange_opportunities
        }

    def analyze_results(self, opportunities):
        triangular_df = pd.DataFrame(opportunities['triangular'])
        cross_exchange_df = pd.DataFrame(opportunities['cross_exchange'])
        
        summary = {
            'triangular': {
                'total_opportunities': len(triangular_df),
                'average_profit': triangular_df['profit'].mean() if not triangular_df.empty else 0,
                'max_profit': triangular_df['profit'].max() if not triangular_df.empty else 0,
                'min_profit': triangular_df['profit'].min() if not triangular_df.empty else 0,
                'profit_distribution': triangular_df['profit'].describe().to_dict() if not triangular_df.empty else {},
                'opportunities_by_exchange': triangular_df['exchange'].value_counts().to_dict() if not triangular_df.empty else {},
                'opportunities_by_path': triangular_df['path'].value_counts().to_dict() if not triangular_df.empty else {}
            },
            'cross_exchange': {
                'total_opportunities': len(cross_exchange_df),
                'average_profit': cross_exchange_df['profit'].mean() if not cross_exchange_df.empty else 0,
                'max_profit': cross_exchange_df['profit'].max() if not cross_exchange_df.empty else 0,
                'min_profit': cross_exchange_df['profit'].min() if not cross_exchange_df.empty else 0,
                'profit_distribution': cross_exchange_df['profit'].describe().to_dict() if not cross_exchange_df.empty else {},
                'opportunities_by_pair': cross_exchange_df['pair'].value_counts().to_dict() if not cross_exchange_df.empty else {}
            }
        }
        return summary