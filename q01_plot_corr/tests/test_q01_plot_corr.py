import pandas as pd
from unittest import TestCase
from ..build import plot_corr
from inspect import getargspec

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPlot_corr(TestCase):
    def test_plot_corr(self):
        # Input parameters tests
        args = getargspec(plot_corr)
        self.assertEqual(len(args[0]), 2, "Expected arguments %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], 11, "Expected default values do not match given default values")

        # Return type tests
        # Nothing to check here

        # Return value tests
        # Nothing to check here
