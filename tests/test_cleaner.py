import unittest
import pandas as pd
from src.data_cleaner import clean_data

class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.dirty_df = pd.DataFrame({
            'Age': [25, None, 30],
            'Salary': [50000, 60000, None],
            'Gender': ['Male', None, 'Female']
        })

    def test_clean_data_removes_missing(self):
        clean_df = clean_data(self.dirty_df)
        self.assertEqual(clean_df.isnull().sum().sum(), 0)  # no missing values
        self.assertLess(len(clean_df), len(self.dirty_df))  # some rows dropped

if __name__ == '__main__':
    unittest.main()
