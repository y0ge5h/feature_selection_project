# Plot a correlogram for all numeric variables

Correlation gives us the idea about how the are the features related to the target variable
and gives us the idea which variables would have significant impact on target variable.

## Write a function `plot_corr` that:
- Should return plots of numeric variables.
- As we require plot, type of return variable should be matplotlib object.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | Input DataFrame |
| size| Integer | compulsory |  | Input size of the graph  |


### Returns:

Correlation plot for all numeric variables.