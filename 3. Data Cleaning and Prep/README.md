# Missing Data/NULL Values

__Remove Duplicates:__ <br>
Pro: Easy and quick process. This is good for samples with a very small proportion of missing data <br>
Con: Could be detrimental if empty rows actually mean something. ex: call time of NA means a hang up at a telemarketer center <br>
So in this case, just deleting the null values would be deleting a whole category of outcomes and thus creating biased data <br><br>

__Masking/Assigning Categories:__ <br>
Creating a category for missing values. This assumes that the missing values actually mean something <Br>
Pro: You don't lose any data <br>
Con: The assumption that the missing values have meaning adds a level of uncertainty to data. Can we really be sure that all the cases of null values mean the same thing? <br><br>

__Impute data:__ <br>
Replace null values with substituted values (mean, median, mode)<br>
Pro: You don't lose any data <br>
Con: The calculated values that will replace the null values will never be truly accurate. And it is impossible to know how close or how far off from the real values our imputed values will be.

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


- Prepping Data
- Splitting the Data
- Transformations
- Normalization
- Dimension Reduction
- Dummy Variable Creation
