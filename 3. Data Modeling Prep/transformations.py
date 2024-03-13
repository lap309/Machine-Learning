"""Transformations: Changing features to maintain a linear model
Necessary if the raw data/scatter plot is not actually linear or if it exhibits a curved pattern, indicating a more complicated relationship between x and y.
If x and y are not linear, then we want to add polynomial features to the equation to help the model predict the relationship between x and y.
The process is similar to what we would do for a linear relationship, we are just choosing a curve instead of a line.
We choose an appropriate curve, evaluate the fit of the curve, and use a residual plot to assess whether the curve is an appropriate way to describe the relationship.
If the curve is a useful summary of the relationship, then we can use it to make predictions.

General strategy for fitting a nonlinear model is to find a way to transform the x or y values so the values in the scatterplot have a linear appearance.

Common functions:
Quadratic/Polynomial y = a+bx + x^2
Square Root          y = a + ( b*sqrt(x) )
Reciprocal           y = a + ( b * (1/x) )
Log Function         y = a + ( b*ln(x) )
Exponential          y = e ^ (a+bx)
Power Function       y = ax^b
"""

########## Log Transformation
#Good if the data has diminishing returns"""

from numpy import log, log1p
from scipy.stats.import boxcox
import seaborn as sns

#use log1p if you have 0s in your dataset: log1p is the log+1 because you can't take the log of 0
#boxcox will find the ideal way to transform from a skewed dataset (left/right skewed)

#Apply log transformation
log_data = [math.log(x) for x in data['col_name']]

#alternative way to log transform
#log_data = np.log(df['col'])

# plot transformed plots
sns.displot(log_data, bins=20)

########## Polynomial Features
# Estimate higher-order relationships by adding polynomial features to add more flexibility to the model

from sklearn.preprocessing import PolynomialFeatures
#create an instance of the transformer object
polyfeat_transform = PolynomialFeatures(degree=2)

#fit and transform to the data
x_poly = polyfeat_transform.fit(x).transform(x)
