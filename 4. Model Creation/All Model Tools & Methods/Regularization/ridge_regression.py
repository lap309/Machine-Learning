

# we want to optimize to find the best alpha/regularization hyperparameter that will avoid overfitting and help the model generalize for all types of data
alpha = np.geomspace(0.1, 2, 20)

#alpha is a buffer applied to the data that will reduce complexity. So the higher alpha, the less complex the model would be (the lower the alpha, the more complex)
#having no alpha at all would be the same as a linear regression
#lasso and ridge iteratively runs a for loop on the backend to find the optimal radiant descent. If you don't let it run enough iterations, it won't converge and find that optimal value
lasso = Lasso(alpha=alpha, amx_iter=100000)

ridge =Ridge(alpha=alpha, max_iter=100000)
