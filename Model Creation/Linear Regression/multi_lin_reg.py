# assumes normality has been checked and transformations are applied


import pandas as pd
import sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


"""Pre-Model ASSUMPTIONS AND DATA PREP"""
####### Assess Linearity between independent variables and target variables
# would need to do this for every single variable
fig, (ax1, ax2) = plt.subplots(figsize = (12,8), ncols=2,sharey=False)
sns.scatterplot( x = data['col1'], y = data['target_variable'],  ax=ax1)
sns.regplot(x=data['col1'], y=data['target_variable'], ax=ax1)

sns.scatterplot(x = data['col2'],y = data['target_variable'], ax=ax2)
sns.regplot(x=data['col2'], y=data.['target_variable'], ax=ax2)

###### ASSESS Linear CORRELATIONS FOR INDEPENDENT ~ DEPENDENT VARIABLES (if not significant, drop from model)
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

######### CHECK FOR MULTICOLlINEARITY
plt.figure(figsize = (30, 25)) sns.heatmap(data.corr(), annot = True, cmap="YlGnBu") plt.show()


######### MAKE THE MODEL
lr = LinearRegression()            # instantiate
lr = lr.fit( x_train, y_train)     # fit to data

######### EVALUATE THE MODEL
lm.score(X_train,y_train)             # The score() method returns the coefficient of determination of the prediction.
r2_score(y_test,predictions)          # could also use r2_score, it's the same thing

######### MAKE PREDICTIONS
predictions = lr.predict(y_test)    # predict val
r2_score(y_test,predictions)

mse_prdictions = mean_squared_error(y_test, predictions)

# R-squared - % of the variance in our dependent variable (y) that can be explained by the model
# Can be read that as x increases by 1, y is affected by the returning variable coefficient number
# p_value < .05 means we reject the null hypothesis and the coefficient is statistically significant. Remove any variables that have a p|t|>0.05
# confidence interval [lower bound < 0 < upper bound] indicates we do not reject null hypothesis

###### PLOTTING RESIDUALS
plt.subplots(figsize = (12,8))
sns.residplot(x=data["enginesize"], y=data["price"])

###### Assessing for Normality after the Model
## Necessary packages for the below definition
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
import matplotlib.style as style
style.use('fivethirtyeight')


def plotting_3_chart(data, feature):
    ## Creating a customized chart. and giving in figsize and everything. 
    fig = plt.figure(constrained_layout=True, figsize=(12,8))
    ## creating a grid of 3 cols and 3 rows. 
    grid = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    #gs = fig3.add_gridspec(3, 3)

    ## Customizing the histogram grid. 
    ax1 = fig.add_subplot(grid[0, :2])
    ## Set the title. 
    ax1.set_title('Histogram')
    ## plot the histogram. 
    sns.distplot(data.loc[:,feature], norm_hist=True, ax = ax1)

    # customizing the QQ_plot. 
    ax2 = fig.add_subplot(grid[1, :2])
    ## Set the title. 
    ax2.set_title('QQ_plot')
    ## Plotting the QQ_Plot. 
    stats.probplot(data.loc[:,feature], plot = ax2)

    ## Customizing the Box Plot. 
    ax3 = fig.add_subplot(grid[:, 2])
    ## Set title. 
    ax3.set_title('Box Plot')
    ## Plotting the box plot. 
    sns.boxplot(data.loc[:,feature], orient='v', ax = ax3);
    
plotting_3_chart(data, 'target_var')
