
__Model Overfitting__ <br>
* Regularization (Lasso, Ridge, etc)

__Model Underfitting__ <br>
* Cross Validation

## Regularization
!!!! DATA MUST BE SCALED FIRST. Otherwise it will lead to excessive penalties
Used to avoid overcomplicating the data and overfitting. 
Meant to reduce overfitting, make the model flexible for other datasets, and reduce variance between future samples<br><br>
Acts second handedly as feature selection. Because we are attributing a penalty for having a more complex model, the more features you have in the model, the more compelx the model will be. So it may lead to eliminating some features, and selecting which ones to include in the model. This elimination happens automatically when we run regularization though<br><br>

The regularization portion is just added on to the original cost function of the model (which we want to minimize). The more complex the model is, the larger lambda becomes, and the larger our cost function will be, which is not ideal and not the goal. And so, the regularization portion added on to the model cost function acts as a penalty to the model if the model gets too complex.
$$Model cost function = Model error + \lambda{R(w)}$$

where our R is just going to be a function of the strength of our different parameters (coefficients), and $\lambda$ adds a penalty proportion to the size of the strength of these parameters or some function of these parameters. So the more parameters you have, the stronger the model, or the stronger/larger effect the parameters have (hence the need for scaling) >> the larger the regularization portion will be. <br>
And the larger the regulatization portion, the larger the model cost function is, which makes it non-ideal, thus regularization penalizes the model if it is overcomplex. This prevents us from choosing models that are too complex, too accurate, and thus, overfit. <br> <br>


Increasing $\lambda$ >> a higher penalty >>so more penalty for larger coefficients >> the less complex the model will be >>less variability (but potentially more bias)<br>
Increasing $\lambda$ also decreases each one of the coefficients in the model

There are several different types of regularization, and the difference is just between how the coefficients are penalized

__Lasso (L1)__ <br>
Lambda proportionally penalizes to the absolute value of coefficients. <br><br>
Lasso is more likely to preform feature selection because it is more likely to completely zero out certain coefficients >> eliminating features/performing feature selection (good for interpretability) <br>
$$RSS + \lambda{\sum}{|\beta_j|} $$

$\beta_j$ = coefficient

The effect of using the absolute value is it's going to selectively shrink some coefficients compared to Ridge, which is more likely to shrink all the coefficients at once.<br><br>

Increasing Lambda >> rhigher penalization >> emoves more coefficients in the model

__Ridge Regression (L2)__ <br>
Lambda proportionally penalizes parameters by the square of the coefficients. So larger coefficients will have a higher penalization. That's why scaling is so important to implement if you're going to use regularization<br>
$$RSS + \lambda{\sum}{\beta_j^2} $$

$\beta_j$ = coefficient

The higher the weights are >> the higher the coefficient >> the more that is added to the cost function >> the more the model is penalized <br>
This is a result of the squaring term in the errors function. As coefficients get large, their squared values will be exponentially larger, therefore making the penalization term larger for larger coefficients. <br>
<br>
This also means that smaller coefficients will 

#### Note** LAsso vs. Ridge
Ridge is more computationally efficient than Lasso and faster to converge.<br>
But Lasso will eliminate some of the coefficients which can be better interpretability<br> <br>


__Elastic Net__ <br>
A combination of Ridge and Lasso
$$\lambda{\sum}{\alpha}{\beta_j^2}+{(1-\alpha)}{|\beta_j|}$$
$$RSS+ lambda_1{\sum}{\beta_j^2}+\lambda_2{\sum}{|\beta_j|}$$

$\beta_j$ = coefficient<br>
$\alpha$ = the % that you attribute to the L2 and L1 coefficients

Allows you to allocate a different lambda value depending on Whether you want to attribute more weight to the square or absolute value of the coefficients, but it gives you the option.

The idea here being that you have your lambda all the way out here to the left, decide the portion you want to penalize higher coefficients in general. And then the alpha value that we see will represent the percentage that you attribute to the L2 and L1 weights, to the Ridge and regression weights

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
