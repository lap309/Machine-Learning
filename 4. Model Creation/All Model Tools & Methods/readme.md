
__Model Overfitting__ <br>
* Regularization (Lasso, Ridge, etc)

__Model Underfitting__ <br>
* Cross Validation

## Regularization
!!!! DATA MUST BE SCALED FIRST. Otherwise it will lead to excessive penalties
Used to avoid overcomplicating the data and overfitting. Made to make the model more general and applicable to unseen data or other datasets with the same features<br>
Meant to reduce overfitting<br><br>
Acts second handedly as feature selection. Because we are attributing a penalty for having a more complex model, the more features you have in the model, the more compelx the model will be. So it may lead to eliminating some features, and selecting which ones to include in the model. This elimination happens automatically when we run regularization though<br><br>

The regularization portion is just added on to the original cost function of the model (which we want to minimize). The more complex the model is, the larger lambda becomes, and the larger our cost function will be, which is not ideal and not the goal. And so, the regularization portion added on to the model cost function acts as a penalty to the model if the model gets too complex.
$$Model cost function = Model error + \lambda{R(w)}$$

where our R is just going to be a function of the strength of our different parameters (coefficients), and $\lambda$ adds a penalty proportion to the size of the strength of these parameters or some function of these parameters. So the more parameters you have, the stronger the model, or the stronger/larger effect the parameters have (hence the need for scaling) >> the larger the regularization portion will be. <br>
And the larger the regulatization portion, the larger the model cost function is, which makes it non-ideal, thus regularization penalizes the model if it is overcomplex. This prevents us from choosing models that are too complex, too accurate, and thus, overfit. <br> <br>


Increasing lambda means a higher penalty, so more penalty for stronger weights >> the less complex the model will be <br>

__Lasso__ <br>
Will eliminate features that are not as important (good for interpretability)


__Ridge Regression__ <br>
$$RSS + \lambda{\sum}{weights^2} $$

The higher the weights are >> the higher the coefficient >> the more that is added to the cost function >> the more the model is penalized
More computationally efficient than Lasso<br>
Proportionally penalizes parameters by their strenght. So stronger parameters will have a higher pnealization/lambda?

__Elastic Net__ <br>
A cobination of Ridge and Lasso

## Cross Validation
splits up the data to create several subgroups that helps generalize the data and hyperparameter tuning<br>
Built off of K-folds <br> <br>

## Pipelines

## GridSearchCV
combines cross validation, hyperparameter tuning, and scoring all in one function <br><Br>

Grid Search <br>
- scans over a dictionary of parameters
- finds the hyperparameter set that has the best out-of-sample score
- will keep a copy of the data with the best hyperparameters
- -commonly used in cross validation
