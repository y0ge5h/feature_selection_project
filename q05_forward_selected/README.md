# Building a forward selection from scratch
You should be exicted as ,
In this assignment we are going to build and improvise the forward selection technique from scratch.
Forward Selection chooses a subset of the predictor variables for the final model.Forward selection is a very attractive approach, because it's both tractable and it gives a good sequence of models.

## Write a function `forward_selected` that :
- Performs forward selection technique and selects the best subest of predictor variables for your model.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| data | DataFrame | compulsory |  | Input DataFrame |
| target| string | compulsory |  | target variable |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|model ||an "optimal" fitted statsmodels linear model with an intercept selected by forward selection evaluated by adjusted R-squared|

Hint : Use import statsmodels.formula.api as smf package to predict.
