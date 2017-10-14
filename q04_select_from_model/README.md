# Use SelectFromModel to eliminate one or more than one features

In this assignment we will try to implement the one of the multivariate methods of
feature selection 

## Write a function `select_from_model` that:
- Should return a list of features which are retained.
- The seed should be set as 9.


## Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | Input DataFrame |
| predictors| List | compulsory |  | List of predictor variable names |
| target| string | compulsory |  |  Name of the target variable|


#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|list |List|List of variables which are retained|
