import seaborn as sns

# Histogram
sns.distplot(data, bins=20)

#Boxplot
sns.boxplot(data)

##### Interquartile Range
import numpy as np
q25, q50, q75 = np.percentile(data, [25,50,75])
iqr=q75-q25

min= q25- 1.5*iqr
max = q75+ 1.5*iqr

#print out the outliers
x for x in data['col_name'] if x>max or x<min
