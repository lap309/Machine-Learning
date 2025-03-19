# Supervised Anomaly Detection
When the data is labeled and known as either inlier or outliers (normal or anomaly). <br>
This method is good for known outlier detection but is not capable of discovering unknown anomalies or predicting future issues <br>

| Common Models                                    | Description|
| -------------------------------------------------| ------- |
| Logistic Regression                              | $250    |
| Binary Classification System (Random Forest, Decision Trees)    | modifies it's classification tasks to treat one class as anomalies and the other as normal data |
| K-Nearest Neighbors (KNN)                        | adapted for anomaly detection by using the distance to the kth nearest neighbor as a measure of anomaly. It classifies data points as anomalies if they are significantly different from their k-nearest neightbor    |
| One Class Support Vector Machines                | constructs a hyperlane to learn to distinguish the  majority class (normal) from the minority class (anomalies) |
| XGBoost                                          | $250    |
| Neural Networks                                  | $80     |
| Local outlier factor (LOF)                       | similar to KNN but uses the pints that are furtherst apart to draw conclusions whereass KNN makes assumptions based on data points that are closest together   |
| Decision Trees                                   | $250    |
| Ensemble Methods (AdaBoost and Gradient Boosting | $80     |
| Extreme Value Theory (EVT)                       | used to model the tail distribution of data and detect anomalies ine xtremel values by comparing them to the modeled distribution    |
| Support Vector Data Description (SVDD)           | variation of support vector machines that constructs a hypershphere around normal data points and classifies anomalies as points outside the hemisphere |

