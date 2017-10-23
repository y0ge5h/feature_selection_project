# Default imports
import pandas as pd
import statsmodels.formula.api as smf

data = pd.read_csv('data/house_prices_multivariate.csv')
data.rename(columns={'1stFlrSf': 'FirstFlrSf', '2ndFlrSf': 'SecondFlrSf', '3SsnPorch': 'ThirdSsnPorch'},
            inplace=True)


# Your solution code here

