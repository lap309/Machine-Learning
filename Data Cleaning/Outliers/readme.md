# Identifying Outliers

__Plots__
- Histogram
- Density Plot
- Box Plot

__Statistics__
- IQ Range Box Plot
- Standard Deviation

__Residuals__
-Checking Residuals

# Handling outliers
__Removing Outliers__
Pro: no more outliers <br>
Con: may have lost an important value, or observation that might be helpful to the model

__Assign a new value to the outlier__
Pro: no more outliers, and you can keep all the original observations <br>
Con: You are still losing the original value of the data point

__Transform__
ex: Log transformations

__Imputation__
Ex: Regression
Pro: no more outliers, may be a more accurate value, and keep all the original observations <br>
Con: Requires a lot more work than the other options, 

__Residuals__ (assumes you already have a model) <br>
The difference betwen the actual and predicted values of the outcome variable <br>
- Standardized- residuals divided by the standard error
- Deleted- remove the outlier from the dataframe, then re-run the new model and see if there's a big difference between the original model and the model with the deleted observation
- Studentized- take the deleted residuals, rerun the model, then take the standardization of that rerun, and apply it to the original observation

  


