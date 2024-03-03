#Transformations: Changing features to maintain a linear model

########## Log Transformation
"""Good for linear regression if the raw data is not actually linear or if the data has diminishing returns"""

from numpy import log, log1p
from scipy.stats.import boxcox
import seaborn as sns

#use log1p if you have 0s in your dataset: log1p is the log+1 because you can't take the log of 0
#boxcox will find the ideal way to transform from a skewed dataset (left/right skewed)

#Apply log transformation
log_data = [math.log(x) for x in data['col_name']]

# plot transformed plots
sns.displot(log_data, bins=20)

########## Polynomial Features
# Estimate higher-order relationships by adding polynomial features to add more flexibility to the model

