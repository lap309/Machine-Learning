# assumes normality has been checked and transformations are applied




import pandas as pd
import sklearn.linear_model import LinearRegression

###### ASSESS CORRELATIONS FOR INDEPENDENT ~ DEPENDENT VARIABLES (if not significant, drop from model)
def correlations(data, target_var, print_results=True):
  sig_column = []
  nonsig_column = []
  for col in data.select_dtypes('number').columns:
      p_value = stats.pearsonr(data[col],data[target_var])
      if p_value[1]< 0.05:
         sig_column.append(col)print(col, p_value[1])
      else:
        nonsig_column.append(col)
      if print_results==True:
        print(col, p_value[1])
  print('Columns of Significance: ', sig_column)
  print('Non-significant: ',nonsig_column)

######### MAKE THE MODEL
lr = LinearRegression()            # instantiate
lr = lr.fit( x_train, y_train)     # fit to data


######### MAKE PREDICTIONS
predictions = lr.predict(y_test)    # predict val
r2_score(y_test,lr_pred)


# R-squared - % of the variance in our dependent variable (y) that can be explained by the model
# Can be read that as x increases by 1, y is affected by the returning variable coefficient number
# p_value < .05 means we reject the null hypothesis and the coefficient is statistically significant. Remove any variables that have a p|t|>0.05
# confidence interval [lower bound < 0 < upper bound] indicates we do not reject null hypothesis

###### PLOTTING RESIDUALS
