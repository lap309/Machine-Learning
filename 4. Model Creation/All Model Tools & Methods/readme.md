
__Model Overfitting__ <br>
* Regularization (Lasso, Ridge, etc)

__Model Underfitting__ <br>
* Cross Validation

## Regularization
!!!! DATA MUST BE SCALED FIRST
Used to avoid overcomplicating the data and overfitting. Made to make the model more general and applicable to unseen data or other datasets with the same features
__Lasso__

__Ridge Regression__

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
