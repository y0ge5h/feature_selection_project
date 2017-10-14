# Find most informative features with incorporation of k percentile method.

That's quite an impressive streak you have achieved.

Now let's look at most important features.Since you have learned the technique of selecting `k best features` in lecture.
Here, by doing this assignment you can learn how to implement techniques such as `k percentile` feature selection
which would give you k most important features.


## Write a function `percentile_k_features` that:

- Should return list of k best features with implementation of k percentile  method.



### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | Input DataFrame |
| predictors| List | compulsory |  | List of predictor variable names |
| target| string | compulsory |  | Name of target variable |
| k| integer | compulsory |  | number as int for number of best features required|
| Model| default | optional | None | Takes in Specified model,else if None then selects f regressor model |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|list |List|List of  k important features|

Note: If model value is specified as none then the function should select f regression model as basic model to operate upon, else the function should pass if any model is specified.
