from sklearn.linear_model import Ridge, Lasso

# we want to optimize to find the best alpha/regularization hyperparameter that will avoid overfitting and help the model generalize for all types of data
alpha = np.geomspace(0.1, 2, 20)

#alpha is a buffer applied to the data that will reduce complexity. So the higher alpha, the less complex the model would be (the lower the alpha, the more complex)
#having no alpha at all would be the same as a linear regression
#lasso and ridge iteratively runs a for loop on the backend to find the optimal radiant descent. If you don't let it run enough iterations, it won't converge and find that optimal value

#Lasso REgularization
lasso = Lasso(alpha=alpha, max_iter=100000)
lasso = lasso.fit(x_train, y_train)

pd.DataFrame(lasso.coef_.ravel())
y_pred_las = lasso.predict(x_train)


#Ridge Regularization
ridge =Ridge(alpha=alpha, max_iter=100000)
ridge = ridge.fit(x_train, y_train)

pd.DataFrame(ridge.coef_.ravel())
y_pred_ridge = ridge.predict(x_train)

### Plotting the predictions from each version (optional)
# Predicted Values plot: raw training data, and predicted values from ridge and lasso regularization
plt.plot(x_train, y_train, marker='o', ls='', label='train data')
plt.plot(x_train, y_pred_ridge, label='ridge regression', marker='^', alpha=.5)
plt.plot(x_train, y_pred_las, label='lasso regression', marker='^', alpha=.5)
#plt.plot(X_data, Y_pred, label='linear regression', marker='^', alpha=.5)    # if you've also done the linear regression

plt.legend()
ax = plt.gca()
ax.set(xlabel='x data', ylabel='y data');

# Coefficient regularization effect Plot
# The plot of the predicted values
# Setup the dual y-axes
ax1 = plt.axes()
ax2 = ax1.twinx()
colors = sns.color_palette()

# Plot the linear regression data
ax1.plot(lasso.coef_.ravel(), 
         color=colors[0], marker='o', label='lasso regression')

# Plot the regularization data sets
ax2.plot(ridge.coef_.ravel(), 
         color=colors[1], marker='o', label='ridge regression')
# Customize axes scales
ax1.set_ylim(-2e14, 2e14)
ax2.set_ylim(-25, 25)

# Combine the legends
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2)

ax1.set(xlabel='coefficients',ylabel='linear regression')
ax2.set(ylabel='ridge and lasso regression')

ax1.set_xticks(range(len(lr.coef_)));
