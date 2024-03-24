# Cross Validation
Taking part of our trianing set and using it as 'validation', resampling to create several training sets and validation sets (each slighty different), allowing us to guide our model while making it without compromising our final test data. The point of resampling provides several distributions and more insight when in the process of building the model. The disributions from cross validation will be averaged to give an estimate of the model's predictive performance.

#### Pros/Use Cases:
* Helps avoid Overfitting by creating more opportunities to train the model on your data
* Hyperparameter Tuning

Training on test data runs the risk of overfitting. Cross-Validation trains on multple, subtly-different versions of the data, allowing generalization outside of the specific training set.

### K-fold Cross Validation
Cross validatiom is built off of K-folds. Here are some things to keep in mind.<br>
Notes: <br>
- The number of _k_ will create _k_ subgroups, where each subgorup is used as a test set in k-fold cross-validation
- Increasing k will ___ affect the variance of estimated parameters
- For low complexity models, smaller _k_ will reduce or eliminate underfitting ????
- For high complexity models, a high variance of parameter estimates across cross-valildation subsamples indicates overfitting
- For low complexity models, assuming there is enough trainind data, the number of _k_ folds does not inherently result in underfitting


- K-fold Cross validation: k indicates the number iterations of training/testing sets we want to create. So we partition the data. fit the model to the training set, evaluate performance, then repeat k times.
- Leave one out Cross Validation: Similar idea to K-fold, except there are more folds. One fold per data point and on each fold, we leave out one data point for validation and use the rest for training.
- Stratified K-fold
- Group K-fold


