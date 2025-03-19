# Supervised Anomaly Detection
When the data is labeled and known as either inlier or outliers (normal or anomaly). <br>
This method is good for known outlier detection but is not capable of discovering unknown anomalies or predicting future issues <br>

| Common Models                                    | Description|
| -------------------------------------------------| ------- |
| Logistic Regression                              | $250    |
| Binary Classification System                     | $80     |
| K-Nearest Neighbors (KNN)                        | $420    |
| One Class Support Vector Machines                |         |
| XGBoost                                          | $250    |
| Neural Networks                                  | $80     |
| Local outlier factor (LOF)                       | similar to KNN but uses the pints that are furtherst apart to draw conclusions whereass KNN makes assumptions based on data points that are closest together   |
| Random Forest                                    |         |
| Decision Trees                                   | $250    |
| Ensemble Methods (AdaBoost and Gradient Boosting | $80     |
| Extreme Value Theory (EVT)                       | used to model the tail distribution of data and detect anomalies ine xtremel values by comparing them to the modeled distribution    |
| Support Vector Data Description (SVDD)           | variation of support vector machines that constructs a hypershphere around normal data points and classifies anomalies as points outside the hemisphere |

