# Building a forward selection from scratch
* As there is no package for forward selection we will gonna build it by own
* for this we have used import statsmodels.formula.api as smf package to predict.

## Write a function

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| data | DataFrame | compulsory |  | Input DataFrame |
| target| string | compulsory |  | target variable |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|model ||an "optimal" fitted statsmodels linear model with an intercept selected by forward selection evaluated by adjusted R-squared|