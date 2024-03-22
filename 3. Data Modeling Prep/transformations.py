"""Transformations: Changing features to maintain a linear model
General strategy for fitting a nonlinear model is to find a way to transform the x or y values so the values in the scatterplot have a linear appearance.

Necessary if the raw data/scatter plot is not actually linear or if it exhibits a curved pattern, indicating a more complicated relationship between x and y.
If x and y are not linear, then we want to add polynomial features to the equation to help the model predict the relationship between x and y.
The process is similar to what we would do for a linear relationship, we are just choosing a curve instead of a line.
We choose an appropriate curve, evaluate the fit of the curve, and use a residual plot to assess whether the curve is an appropriate way to describe the relationship.
If the curve is a useful summary of the relationship, then we can use it to make predictions.



Common functions:
Quadratic/Polynomial y = a+bx + x^2
Square Root          y = a + ( b*sqrt(x) )
Reciprocal           y = a + ( b * (1/x) )
Log Function         y = a + ( b*ln(x) )       Helpful with outliers
Exponential          y = e ^ (a+bx)
Power Function       y = ax^b
"""

########## Log Transformation
#Good if the data has diminishing returns"""

from numpy import log, log1p
from scipy.stats.import boxcox
import seaborn as sns
from scipy.stats.mstats import normaltest # D'Agostino K^2 Test: test for normality. 

#use log1p if you have 0s in your dataset: log1p is the log+1 because you can't take the log of 0
#boxcox will find the ideal way to transform from a skewed dataset (left/right skewed)

##########################################################
                    #   Apply log transformation
##########################################################
log_data = [math.log(x) for x in data['col_name']]

log_data = np.log(df['col'])   #alternative way to log transform
log_data = np.log(data)        # Log transformation (base e)
log10_data = np.log10(data)    # Log transformation (base 10)

#  plot transformed plots
sns.displot(log_data, bins=20)
log_data.hist()

#check for normality with transformed data
normaltest(log_data)

##########################################################
                    #   Square Root Transformation
##########################################################
 squared_data = np.sqrt(data['col'])

# Plot square root data
plt.hist(np.sqrt(squared_data))

# test for normality of squared data
normaltest(squared_data)

##########################################################
                    #   Box Cox Transformation
##########################################################
from scipy.stats import boxcox
# will give an array of outputs, the first item being the transformed data, the second item being the value of lambda used in the boxcos transformation equation
boxcox_transform = boxcox(data['col'])
boxcox_data = boxcox_transform[0]
boxcox_lambda = boxcox_transform[1]


#plotting
plt.hist(boxcox_data)
plt.show()

#checking normality for boxcox data
normaltest(boxcox_data)


########## Polynomial Features
# Estimate higher-order relationships by adding polynomial features to add more flexibility to the model

from sklearn.preprocessing import PolynomialFeatures
#create an instance of the transformer object
polyfeat_transform = PolynomialFeatures(degree=2)

#fit and transform to the data
x_poly = polyfeat_transform.fit(x).transform(x)
