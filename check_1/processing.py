import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, db_path):
        self.db_path = db_path

    def inspect_data_structure(self, ticker_data: List[Dict[str, Any]]):
        """
        Inspect and compare the data structure from different exchanges.
        """
        exchange_structures = {}
        for item in ticker_data:
            exchange = item.get('exchange', 'unknown')
            if exchange not in exchange_structures:
                exchange_structures[exchange] = {}
            
            self.update_structure(exchange_structures[exchange], item)

        self.print_comparison(exchange_structures)

    def update_structure(self, structure: Dict[str, str], item: Dict[str, Any]):
        for key, value in item.items():
            if key == 'info' and isinstance(value, dict):
                for info_key, info_value in value.items():
                    info_key_name = f"info_{info_key}"
                    structure[info_key_name] = type(info_value).__name__
            else:
                structure[key] = type(value).__name__

    def print_comparison(self, exchange_structures: Dict[str, Dict[str, str]]):
        all_keys = set()
        for structure in exchange_structures.values():
            all_keys.update(structure.keys())
        
        print("\nData Structure Comparison:")
        print("=" * 80)
        print(f"{'Field':<30} | " + " | ".join(f"{exchange:<15}" for exchange in exchange_structures.keys()))
        print("-" * 80)
        
        for key in sorted(all_keys):
            print(f"{key:<30} | " + " | ".join(f"{exchange_structures[exchange].get(key, 'N/A'):<15}" for exchange in exchange_structures.keys()))

    def process_ticker_data(self, ticker_data: List[Dict[str, Any]]):
        if not ticker_data:
            logger.warning("No ticker data to process.")
            return None

        self.inspect_data_structure(ticker_data)
        return len(ticker_data)