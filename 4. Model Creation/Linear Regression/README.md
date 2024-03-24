# Linear Regression / Least Square Regression

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \ldots + \epsilon$$

Creates a linear equation that minimizes the average distance from the line and each data point. Find the line of best fit by minimizing sum of the squared difference between each data point and the trend line.

### Assumptions
1. There is a linear relationship between the dependent and independent variables
    * Make scatter plots between every independent variable and the dependent variable
    * Check correlations of each independent variable and the dependent variable
2. The independent variables are independent of each other (no multicollinearity)
    * Check correlations between all independent variables
3. Errors/Residuals from the regression model are normally distributed (no bias)
    * Look at a histogram of the residuals, do they look normally distributed? <br><br>
__(Multi-Linear Regressions)__
4. Homoscedasticity: Variance of error terms are similar across the values of the independent variables
    * Look at a plot of the residuals vs. fitted values. It should look like random noise.

The first two assumptinos are checked before the model is fit <br>
The last two are checked after the model is fit 

### Correlations
We want to check to make sure there is a correlation

### Measurement and Evaluation

#### MSE - Mean of Squared Errors
Take the errors of each prediction, square them, then take the mean.
$$MSE = \frac{SSE}{n}=\frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y_i})^2$$ 
<br>
#### $R^2$ 
$R^2$ value represents how much of the total variation of the target _y_ value can be explained by our model.<br>
In other words, how well can our model explain the varaince of the target variable _y_ (in percentage) <br>
Usually [0-1] but can sometimes be negative. A negative $R^2$ value means that a horizontal line at the mean of _y_ is better than the model




#### Residuals - Sum of Squared Errors
$$SSE=SSR = \sum_{i=1}^{n} (Y_i - \hat{Y_i})^2$$ 

We want to minimize the SSR
