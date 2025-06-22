import unittest
import pandas as pd
from src.statistics import calculate_statistics

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Age': [25, 30, 35],
            'Salary': [50000, 60000, 70000],
            'Gender': ['Male', 'Female', 'Female']
        })

    def test_calculate_statistics(self):
        stats = calculate_statistics(self.df)
        self.assertIn('mean', stats)
        self.assertIn('median', stats)
        self.assertIn('mode_non_numeric', stats)
        self.assertAlmostEqual(stats['mean']['Age'], 30.0)
        self.assertEqual(stats['mode_non_numeric']['Gender'], 'Female')

if __name__ == '__main__':
    unittest.main()
