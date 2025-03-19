# Unsupervised Anomaly Detection
Data is not labeled, and therefore unsupervised can handle more complex data sets <br>


<ins> Novelty Detection: </ins> the training set does NOT have outliers and is made exclusively of inliers so that the algorithm learns the concept of “normality”. The test set is provided to the model and we want to know if observations in the test set have the same distribution as the train set, using the distribution results to inform us if there are outliers in the test dataset or not


<ins>Outlier Detection: </ins>The training set contains outliers and it is assumed that the number of outliers is small enough in proportion that the model will be able to indicate the difference between outlier and normal behavior



| Common Models                                    | Description|
| -------------------------------------------------| ------- |
| K means Clustering                               |         |
| Hierarchal Clustering                            |         |
| Isolation Forest                                 |         |
| One Class Support Vector Machines                |         |
| DBSCAN                                           | Particularly effective at indentifying clusters of data points in high density regions while labeling data points in low-density regions as anomalies or noise   |
| Autoencoders                         | Consists of an encoder and decoder network to learn compact representation of input data     |
| Spectral clustering                              |         |
| Local Outlier Factors                            |         |
| Isolation Kernel                                 |         |
| Elliptic Envelope                                |         |
| Histogram Based Outlier Detection                |         |
