import unittest
import pandas as pd
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data_success(self):
        df = load_data('../data/raw_data.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_load_data_failure(self):
        df = load_data('../data/non_existent.csv')
        self.assertIsNone(df)

if __name__ == '__main__':
    unittest.main()
