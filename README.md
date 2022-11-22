# Machine-Learning
Giving data and insights to a model that can then learn the rules for itself. With all models, the goal is always to provide a model that minimizes the error

#### Supervised Learning
training data when we have known outcomes and can use that to compare/test the data

#### Unsupervised Learning
training data when we do !NOT! have known outocomes

## Model Types
#### Classification
Predicting a categorical value or outcome

#### Regression
Predicting a continuous variable
However, regression models can be used for both regressoin and classification tasks.
    - Linear : Least squares/Mean Squared Error is used to assess model quality/loss function
    - Logistic : Powerful models that often outperform more sophisticated machine learning models. Log loss is used to assess model quality/loss function
    
## Methods
**Cross Validation** - taking part of our trianing set and using it as 'validation', resampling to create several training sets and validation sets (each slighty different), allowing us to guide our model while making it without compromising our final test data. The point of resampling provides several distributions and more insight when in the process of building the model. The disributions from cross validation will be averaged to give an estimate of the model's predictive performance.
Training on test data runs the risk of overfitting. Cross-Validation trains on multple, subtly-different versions of the data, allowing generalization outside of the specific training set.
       
       - K-fold Cross validation: k indicates the number iterations of training/testing sets we want to create. So we partition the data. fit the model to the training set, evaluate performance, then repeat k times.
       - Leave one out Cross Validation: Similar idea to K-fold, except there are more folds. One fold per data point and on each fold, we leave out one data point for validation and use the rest for training.
