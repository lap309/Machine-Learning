# Linear Regression / Least Square Regression

$$y = \beta_0 + \beta_1 x + \epsilon$$

Creates a linear equation that minimizes the average distance from the line and each data point. Find the line of best fit by minimizing sum of the squared difference between each data point and the trend line.

### Assumptions
1. Features are linearly independent of each other
2. Errors/Residuals in the regression are normally distributed (no bias)
3. There exists a linear relationship between x and y


### Measurement
#### Residuals - Sum of Squared Residuals
$$SSR = \sum_{i=1}^{n} (Y_i - \hat{Y_i})^2$$ 

We want to minimize the SSR
