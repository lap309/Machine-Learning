import pandas as pd
import statsmodel.formula.api as smf

###### Assess CORRELATIONS
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

# define a string formula using column names (column names can't have whitespace)
formula = 'y_col ~ x_col1 + x_col2 + C(x_col3)'   # C(x_col3) indicates that x_col3 is a a categorical variable
model = smf.ols(formula, data= df)
result=model.fit()

result.summary()

# R-squared - % of the variance in our dependent variable (y) that can be explained by the model
# Can be read that as x increases by 1, y is affected by the returning variable coefficient number
# p_value < .05 means we reject the null hypothesis and the coefficient is statistically significant
# confidence interval [lower bound < 0 < upper bound] indicates we do not reject null hypothesis
