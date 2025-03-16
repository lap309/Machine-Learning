import numpy as np


#Note**: A good rule of thumb when deciding the number of bins is to take the square root of the number of observations



########### MATPLOTLIB ##################
import matplotlib.pyplot as plt
n_bins = int(np.sqrt(len(df)))      #takes the square root of the number of rows and converts to an integer
plt.figure(figsize = (8,4))
plt.hist(df, bins = n_bins, color = 'green')
