import numpy as np
import matplotlib.pyplot as plt

########### Histogram ##################
#Note**: A good rule of thumb when deciding the number of bins is to take the square root of the number of observations
n_bins = int(np.sqrt(len(df)))      #takes the square root of the number of rows and converts to an integer
plt.figure(figsize = (8,4))
plt.hist(df, bins = n_bins, color = 'green')

########### Scatterplot ##################
# helps see direction and relationship of data
# outliers will be the highest or lowest points in the plot
#Univariate data
integers = range(len(df))    #creates a list of consecutive integers with the same length as our distribution
plt.figure(figsize=(16,18))
plot.scatter(integers, df, c = 'blue', alpha = 0.5)

#Bivariate data
plt.figure(figsize=(16,18))
plot.scatter(df['x_col'], df['y_col'], c = 'blue', alpha = 0.5)
