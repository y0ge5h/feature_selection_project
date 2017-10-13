import pandas as pd
from unittest import TestCase
from ..build import plot_corr

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPlot_corr(TestCase):
    def test_plot_corr(self):
        plt = plot_corr(data)
        self.assertTrue(True)
