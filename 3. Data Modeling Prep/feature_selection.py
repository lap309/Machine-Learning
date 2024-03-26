### Only selecing attributes that best explain the relationship between the independent variable and the target variable
#There are several methods for feature selection

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

################## Correlation Coefficient and Heatmap
plt.figure(figsize = (18,18))
sns.heatmap(data.corr(),    # calculates correlation coefficient
            annot=True,    # gives the value of the correlation coefficient as well as the color
            cmap='RdYlGn')    # sets the color scheme for the heat map
plt.show()

### Correlation Coefficients and bar plot
df_corr = data.corr()['target_var'].sort_values()
df_corr.plot(kind='bar', figsize = (10,8))

################### Recursive Feature Elimination (REF)
from sklearn.feature_Selection import RFE

rfe_mod = RFE( est = ml_model, n_features_to_select = 15 )          #instantiate

#the model can be a linear regression, a lasso object, or a more complex object. It just needs to have feature importances or coefficients
rfe_mod=rfe_mod.fit(x_train, y_train)                           # fit
y_pred = rfe_mod.predict(x_test)                                   # predict
