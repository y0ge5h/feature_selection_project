# Find most informative features which fall under k-th percentile.

That's quite an impressive streak you have achieved.

Now let's look at most important features.Since you have learned the technique of selecting `k best features` in lecture.
Here, by doing this assignment you can learn how to implement techniques such as `k percentile` feature selection
which would give you most important feature falling under k-th percentile.


## Write a function `percentile_k_features` that:

- Should return a list of features which fall under the k-th percentile.



### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | Input DataFrame |
| predictors| List | compulsory |  | List of predictor variable names |
| target| string | compulsory |  | Name of target variable |
| k| integer | compulsory |  | Input how many variables you want under k-th percentile |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|list |List|List of important variables falling under k-th  percentile |