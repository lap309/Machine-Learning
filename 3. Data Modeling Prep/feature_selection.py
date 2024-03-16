### Only selecing attributes that best explain the relationship between the independent variable and the target variable
#There are several methods for feature selection

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

##### Correlation Coefficient and Heatmap
plt.figure(figsize = (18,18))
sns.heatmap(data.corr(),    # calculates correlation coefficient
            annot=True,    # gives the value of the correlation coefficient as well as the color
            cmap='RdYlGn')    # sets the color scheme for the heat map
plt.show()

### Correlation Coefficients and bar plot
df_corr = data.corr()['target_var'].sort_values()
df_corr.plot(kind='bar', figsize = (10,8))
