# Tyoes of Relational Coefficients for Data

### Covariance(x,y) / Covariance Matrix
Measures the strength of association between two numerical variables <br>
`df.cov()`<br>
`np.cov( x , y )`<br>

$$\text{Cov(x,y)} = \frac{1}{n-1}\sum\limits_{i=1}^{n}(x_i - \overline{x})(y_i - \overline{y})$$

The formula is very similar to the variance formula (hence co-variance). The "co" indicating 2 variables
Covariance is very sensitive to scaling and is not suitable for comparison across different units. For example, we get a covariance value, but we don't really know what that value means because it is dependent on the scale from the original dataset.<br><br>

Ex: covariance of a dataset measured in inches compared to a covariance of the same dataset measured in feet would result in 12x as much, even though they are measuring the same thing. Even though they are measuring the same thing, the covariance would be a product of 12 because of the difference in unit of measurement. For this reason, correlation might be better.<br><br>

## Correlation (Numeric Variables)
Correlation is the normalized value of Covariance, it measures the strength AND direction of a linear association between 2 variables.<br><br>
"'The degree of variation in one dimension that is explained by the other variable"' <br>
It's basically taking the covariance and making it the common factor of standard deviations between both variables, thus making it respective of the scale of both variables and getting rid of the scope issue we currently see with covariance.

### Pearson's Correlation Coefficient ( _r_): Linear
Normalized version of the covariance (follows a similar formula to z-score) that measure LINEAR DEPENDENCE between 2 variables. <br><br>

np.corrcoef(x,y)<br>
`df.corr()` # returns the correlation between all numerical values in a dataset <br>
`stats.pearsonsr( x, y)`<br><br>

It measure the strength and direction of any linear relationship between two numerical variables.  How two or more variables are related to one another. <br>

$\text{Cor}(X,Y) = \frac{\text{Cov(X,Y)}}{\text{SD}(X)\text{SD}(Y)}$

Note: Having a correlation of 0 does not rule out Non-linear relations/patterns between the variables. df.corr() <br><br>

### Spearman's Rank Correlation: Non-linear / non-parametric
Non-parametric measure of rank correlation. This would be like ranking the x values, ranking the y values, then taking the correlation of the new rank columns. This is helpful to identify NON-LINEAR RELATIONSHIPS <br><br>


## Correlation (Non-numeric)

### Phi Coefficient: Binary Categorical Variables
Based off of Pearsons but called MCC(Mathew's Correlation Coefficient) in Machine Learning <br>
Used to evaluate predictions by a binary classifier<br><br>

### Point Biserial Correlation: Binary category and Continuous variable
Based off of Pearsons <br><br>


### $\chi^2$ Chi-Squared Test of Independence: Correlation between 2 categorical/binary variables
Tests whether two vategorical variables are related to each other.
Chi-squared test can answer questions like: <br>
- Are people's favorite color related to their favorite fruit?
- Is there a significant relationship between country of resident and field that they work in?
<br>
Assumptions:<br>
- The data in the cells should be frequencies.
- The levels (or categories) of the variables are mutually exclusive. That is, a particular subject fits into one and only one level of each of the variables.
- Each subject may contribute data to one and only one cell.
- The study groups must be independent.

### Population Correlation Coefficient (_p_)


# Testing Correlation Significance for the Population
When calculating a correlation for a sample, the goal is that it approximates the correlation for the population. For example, if age and weight are correlated in our sample, we want to say that the correlation upholds when we consider all children in the population. To test whether this is true, we can use a hypothesis test. 

- r is the sample correlation
- $\rho$ is the population correlation

**Hypothesis Test**:

$H_0: \rho = 0\;\; vs \;\;  H_1: \rho \neq 0$

**Test Statistic**:

$$ t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}} $$

In the test statistic above, r is the sample correlation coefficient and n is the number of samples. 


The intuition for this test is if we calculate a sample proportion based on a small sample of data points, this might not correctly approximate the population correlation. If we only have two points, the correlation will be 1, but it is unlikely to be a real effect.
