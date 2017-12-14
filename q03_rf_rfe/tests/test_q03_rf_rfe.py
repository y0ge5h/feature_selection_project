import pandas as pd
from unittest import TestCase
from ..build import rf_rfe
from inspect import getargspec

data = pd.read_csv('data/house_prices_multivariate.csv')
expected = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF',
                    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotRmsAbvGrd', 'GarageYrBlt', 'GarageArea',
                    'WoodDeckSF', 'OpenPorchSF', 'YrSold']
top_features = rf_rfe(data)

class TestRf_rfe(TestCase):
    def test_rf_rfe_arguments(self):

        # Input parameters tests
        args = getargspec(rf_rfe)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
    def test_rf_rfe_defaults(self):
        args = getargspec(rf_rfe)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
    def test_rf_rfe_return_instance(self):
        self.assertIsInstance(top_features, list,
                              "Expected data type for return value is `List`, you are returning %s" % (
                                  type(top_features)))

        # Return values tests
    def test_rf_rfe_return_values(self):
        self.assertEqual(top_features, expected, "Expected list of variables does not match returned list of variables")
