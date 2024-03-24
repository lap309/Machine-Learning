**Cross Validation** - taking part of our trianing set and using it as 'validation', resampling to create several training sets and validation sets (each slighty different), allowing us to guide our model while making it without compromising our final test data. The point of resampling provides several distributions and more insight when in the process of building the model. The disributions from cross validation will be averaged to give an estimate of the model's predictive performance.

Training on test data runs the risk of overfitting. Cross-Validation trains on multple, subtly-different versions of the data, allowing generalization outside of the specific training set.
       
- K-fold Cross validation: k indicates the number iterations of training/testing sets we want to create. So we partition the data. fit the model to the training set, evaluate performance, then repeat k times.
- Leave one out Cross Validation: Similar idea to K-fold, except there are more folds. One fold per data point and on each fold, we leave out one data point for validation and use the rest for training.

