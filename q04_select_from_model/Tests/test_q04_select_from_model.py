import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from unittest import TestCase
from ..build import select_from_model
from inspect import getargspec


class TestSelect_from_model(TestCase):
    def test_select_from_model(self):
        # Input parameters tests
        args = getargspec(select_from_model)
        self.assertEqual(len(args[0]), 3, "Expected arguments %d, Given %d" % (3, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
        np.random.seed(9)
        predictors = list(data.columns.values)[:-1]
        target = 'SalePrice'
        expected = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF',
                    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageYrBlt', 'GarageArea', 'WoodDeckSF',
                    'OpenPorchSF', 'YrSold']
        selected_variables = select_from_model(data, predictors, target)
        self.assertIsInstance(selected_variables, list,
                              "Expected data type for return value is `List`, you are returning %s" % (
                                  type(selected_variables)))
        # Return values tests
        self.assertItemsEqual(selected_variables, expected, "Expected list of variables does not match returned list "
                                                            "of variables")
