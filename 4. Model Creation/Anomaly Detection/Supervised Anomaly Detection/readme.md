# Supervised Anomaly Detection
When the data is labeled and known as either inlier or outliers (normal or anomaly). <br>
This method is good for known outlier detection but is not capable of discovering unknown anomalies or predicting future issues <br>

| Common Models                                    | Description| Best for| Challenges |
| -------------------------------------------------| -------    | ---  ---| -----------|
| * Local outlier factor (LOF)                     | Calculates the density of data around a point and compares it to its neighboring data points to determine how isolated the point is relative to it's surroundings. Similar to KNN but uses the points that are furtherst apart to draw conclusions whereass KNN makes assumptions based on data points that are closest together. If a point's density is significantly lower than its neighbors, it is marked as an anomaly  | Non-linear data and complex data sets. Good to detect unusual activity or patterns in logs | Computationally expensive |
| * One Class Support Vector Machines                | Type of SVM designed specifically for Anomaly detection. Constructs a boundary to learn to distinguish the  majority class (normal) from the minority class (anomalies) | small, high-quality data sets with precise boundaries. Common in manufacturing to read machine sensor data| Significantly computationally expensive for large datasets. Performance degreates in high-dimensional data |
| Logistic Regression                              | learns a decision boundary that separates normal and anomalous data points| Point Anomalies| |
| Binary Classification System (Random Forest, Decision Trees, XGBoost)    | modifies it's classification tasks to treat one class as anomalies and the other as normal data | | |
| K-Nearest Neighbors (KNN)                        | adapted for anomaly detection by using the distance to the kth nearest neighbor as a measure of anomaly. It classifies data points as anomalies if they are significantly different from their k-nearest neightbor    | | |
| Ensemble Methods (AdaBoost and Gradient Boosting |      | |
| Extreme Value Theory (EVT)                       | used to model the tail distribution of data and detect anomalies ine xtremel values by comparing them to the modeled distribution  |  | |
| Support Vector Data Description (SVDD)           | variation of support vector machines that constructs a hypershphere around normal data points and classifies anomalies as points outside the hemisphere | | |
| Naive Bayes                                      | models the probability distribution of normal data and identifying deviations from it| | |

https://medium.com/@venujkvenk/anomaly-detection-techniques-a-comprehensive-guide-with-supervised-and-unsupervised-learning-67671cdc9680

