# Transformations: Changing features to maintain a linear model
General strategy for fitting a nonlinear model is to find a way to transform the x or y values so the values in the scatterplot have a linear appearance.<br><br>

Even by adding in polynomials or exponents/squared features/non-linear variables, the formula in the model itself will still be a linear combination (addition) of the variables that we transform <br><br>

Necessary if the raw data/scatter plot is not actually linear or if it exhibits a curved pattern, indicating a more complicated relationship between x and y.<br>
If x and y are not linear, then we want to add polynomial features to the equation to help the model predict the relationship between x and y. <br>
The process is similar to what we would do for a linear relationship, we are just choosing a curve instead of a line. <br>
We choose an appropriate curve, evaluate the fit of the curve, and use a residual plot to assess whether the curve is an appropriate way to describe the relationship. <br>
If the curve is a useful summary of the relationship, then we can use it to make predictions. <br>
<br>
### Common functions:
|_______|_____________|_______________________|
|Quadratic/Polynomial| y = a+bx + x^2|  |
|Square Root   |       y = a + ( b*sqrt(x) )|  |  
|Reciprocal   |        y = a + ( b * (1/x) )|  |
|Log Function   |      y = a + ( b*ln(x) )  |     Helpful with outliers|
|Exponential    |      y = e ^ (a+bx)|  |
|Power Function   |    y = ax^b|  |

## Polynomial Features
Allows you to use a linear model to fit nonlinear data <br>
Also good if the model is underfitting <br>
It combining features together to create interaction terms. <br>
- Multiplying
- Division
- Exponents/Powers
- Square Root
