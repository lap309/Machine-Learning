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

# Encoding / Dummy Variable Creation
Applied to categorical features to give them numeric values <br>
The two types: <Br>
Nominal: categorical variables with NO order ex: [true, false], [red, green, blue]  <br>
Ordinal: categorical variables with an order ex: [high, medium, low], [cold, warm, hot] <Br>
<Br>
Types of Encoding: <br>
* Binary  Encoding- converts variables to 0 or 1
* Hot One Encoding - creates a new column for each value in the original column
* Ordinal Encoding - converting values in the column into an ordered number set ( ex: low = 1, medium = 2, high = 3)

# Splitting the Data

# Transformations: Changing features to maintain a linear model
Necessary if the raw data/scatter plot is not actually linear or if it exhibits a curved pattern, indicating a more complicated relationship between x and y. <Br>
If x and y are not linear, then we want to add polynomial features to the equation to help the model predict the relationship between x and y. <br>
The process is similar to what we would do for a linear relationship, we are just choosing a curve instead of a line. <br>
We choose an appropriate curve, evaluate the fit of the curve, and use a residual plot to assess whether the curve is an appropriate way to describe the relationship. <br>
If the curve is a useful summary of the relationship, then we can use it to make predictions. <br>
<br>
General strategy for fitting a nonlinear model is to find a way to transform the x or y values so the values in the scatterplot have a linear appearance. <br> <br>

| Common Functions       | Type of Data          |
| -----------------------| ----------------------|
| Quadratic/Polynomial   | y = a+bx + x^2        |
| Swuare Root            | y = a + ( b*sqrt(x) ) |
| Reciprocal             | y = a + ( b * (1/x) ) | 
| Log Function           | y = a + ( b*ln(x) )   |
| Exponential            | y = e ^ (a+bx)        | 
| Power Function         |  y = ax^b             |

# Scaling
Adjusting the variables to be on the same scale to allow comparison of variables with different scales when put through the model. <br>

__Standard Scaling__ <br>
z-score scaling / normalization on a bell curve scale <br>
Note** This is sensitive to outliers <br> <br>

__Min-Max Scaler__ <br>
Put all the values between 0 and 1 <br>
(x- min) / (max-min) <br>
Note **  This is heavily sensitive to outliers <br> <br>
 
__Robust Scaling__ <br>
Similar to min-max but it focuses on the interquartile range, which works better with adjusting to outliers <br>
Not between 0 and 1


# Dimension Reduction
