## SCALING HAPPENS AFTER SPLITTING THE TEST AND TRAIN DATA
otherwise we will get data spill and the values in the train data will be affected by the values in the test data <br><br>

Data transformations are necessary to adjust the raw data to optiize the algorithm and model performance

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

| Common Functions       | Type of Data          | When do use         |
| -----------------------| ----------------------|----------------------|
| Quadratic/Polynomial   | y = a+bx + x^2        |     |
| Square Root            | y = a + ( b*sqrt(x) ) |      |
| Reciprocal             | y = a + ( b * (1/x) ) |       | 
| Natural Log Function   | y = a + ( b*ln(x) )   |  reducing the impact of outliers, transforming skewed data to approximate normality, linearizing relationships between variables, and stabilizing variance in heteroscedastic data.      |
| Exponential            | y = e ^ (a+bx)        |      |
| Power Function         |  y = ax^b             |      |

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

