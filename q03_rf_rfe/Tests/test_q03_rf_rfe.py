import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from unittest import TestCase
from q03_rf_rfe.build import rf_rfe


class TestRf_rfe(TestCase):
    def test_rf_rfe(self):
        predictors = list(data.columns.values)[:-1]
        target = 'SalePrice'
        expected = ['LotFrontage',
                    'LotArea',
                    'YearBuilt',
                    'YearRemodAdd',
                    'MasVnrArea',
                    'BsmtFinSF1',
                    'BsmtUnfSF',
                    'TotalBsmtSF',
                    '1stFlrSF',
                    '2ndFlrSF',
                    'GrLivArea',
                    'TotRmsAbvGrd',
                    'GarageYrBlt',
                    'GarageArea',
                    'WoodDeckSF',
                    'OpenPorchSF',
                    'YrSold']

        self.assertEqual(rf_rfe(data, predictors, target), expected)
