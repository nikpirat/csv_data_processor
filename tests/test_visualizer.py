import unittest
import os
import pandas as pd
from src.visualizer import plot_histogram, plot_scatter

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Age': [25, 30, 35],
            'Salary': [50000, 60000, 70000]
        })
        self.hist_path = '../output/plots/test_hist.png'
        self.scatter_path = '../output/plots/test_scatter.png'

    def test_plot_histogram(self):
        plot_histogram(self.df, 'Salary', self.hist_path)
        self.assertTrue(os.path.exists(self.hist_path))

    def test_plot_scatter(self):
        plot_scatter(self.df, 'Salary', 'Age', self.scatter_path)
        self.assertTrue(os.path.exists(self.scatter_path))

    def tearDown(self):
        if os.path.exists(self.hist_path):
            os.remove(self.hist_path)
        if os.path.exists(self.scatter_path):
            os.remove(self.scatter_path)

if __name__ == '__main__':
    unittest.main()
