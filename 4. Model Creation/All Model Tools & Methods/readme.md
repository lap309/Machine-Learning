
__Model Overfitting__ <br>
* Regularization (Lasso, Ridge, etc)

__Model Underfitting__ <br>
* Cross Validation

## Regularization
!!!! DATA MUST BE SCALED FIRST. Otherwise it will lead to excessive penalties
Used to avoid overcomplicating the data and overfitting. 
Meant to reduce overfitting, make the model flexible for other datasets, and reduce variance between future samples<br><br>

#### LASSO (L1)
- Penalizes the absolute value of the coefficients
- Sets irrevelant features to 0
- acts second handedly as feature selection / eliminating features with small significance
- Has better intrepretability because of the feature selection

#### Ridge (L2)
- Penalizes the size magnitude of the regression coefficients by adding a squad term
- Enforces the coefficients to be lower, but not 0
- Minimizes irrelevant features but does not remove them
- Faster to train and more efficient algorithm

#### Elastic Net (L1 + L2)
- Penalizes the size magnitude of the regression and absolute value of the coefficients
- sets irrelevant features to 0 and enforces the coefficients to be lower

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
