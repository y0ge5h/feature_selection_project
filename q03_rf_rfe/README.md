# Use RandomForest RFE to eliminate one or more than one features

You can build a good model just by fewer features rather than including all of them.
Hence, the elimination of features in order to get most significant features can be achieved by using RFE.  This assignment will help you learn to create your own Recursive Feature Elimination function
and help you decide which features are irrelevant and hence can be eliminated. 

## Write a function `rf_rfe` that:
- Uses RandomForest RFE to give out most significant features which are retained.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | Input DataFrame |
| predictors| List | compulsory |  | List of predictor variable names|
| target| string | compulsory |  |  Name of the target variable |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|list |List|List of variables which are retained|
