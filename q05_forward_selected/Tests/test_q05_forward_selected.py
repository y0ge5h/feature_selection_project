from unittest import TestCase
from ..build import forward_selected
from inspect import getargspec
import pandas as pd
data = pd.read_csv('data/house_prices_multivariate.csv')
data.rename(columns={'1stFlrSf': 'FirstFlrSf', '2ndFlrSf': 'SecondFlrSf', '3SsnPorch': 'ThirdSsnPorch'},
            inplace=True)


class TestForward_selected(TestCase):
    def test_forward_selected(self):

        # Input parameters tests
        args = getargspec(forward_selected)
        self.assertEqual(len(args[0]), 2, "Expected arguments %d, Given %d" % (2, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")


        target = 'SalePrice'
        fwd_selection = forward_selected(data, target)
        fwd_selec_value = fwd_selection.rsquared_adj

        # Return values tests
        self.assertItemsEqual(fwd_selec_value, 0.801032497472, "Expected value does not match returned value")