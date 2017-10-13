
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))


from q02_best_k_features.build import percentile_k_features

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from unittest import TestCase


class TestPercentile_k_features(TestCase):
    def test_percentile_k_features(self):
        expected = ['OverallQual', 'GrLivArea',
                    'GarageCars',
                    'GarageArea',
                    'TotalBsmtSF',
                    '1stFlrSF',
                    'FullBath',
                    'TotRmsAbvGrd',
                    'YearBuilt',
                    'YearRemodAdd']
        predictors = list(data.columns.values)[:-1]
        target = 'SalePrice'
        self.assertEqual(percentile_k_features(data, predictors, target, 10), expected)

