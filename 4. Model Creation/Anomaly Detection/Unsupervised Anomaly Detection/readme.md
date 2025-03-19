# Unsupervised Anomaly Detection
Data is not labeled, and therefore unsupervised can handle more complex data sets <br>


<ins> Novelty Detection: </ins> the training set does NOT have outliers and is made exclusively of inliers so that the algorithm learns the concept of “normality”. The test set is provided to the model and we want to know if observations in the test set have the same distribution as the train set, using the distribution results to inform us if there are outliers in the test dataset or not


<ins>Outlier Detection: </ins>The training set contains outliers and it is assumed that the number of outliers is small enough in proportion that the model will be able to indicate the difference between outlier and normal behavior



| Common Models                                    | Description|
| -------------------------------------------------| ------- |
| K means Clustering                               | treats data points in small clusters as anomalies |
| Hierarchal Clustering                            | treats data points in small clusters as anomalies |
| Isolation Forest                                 | ensemble method that isolates anomalies by constructing random forests and isolating data points that require fewer splits in the trees to be isolated |
| Isolation Kernel (iKernel)                       | an extension of Isolation Forest that uses kernel methods to capture non-linear relationships in data   |
| One Class Support Vector Machines                | constructs a hyperplane that separates the majority of the data from potential anomalies. VERY useful when anomalies are rare and not well distributed |
| DBSCAN                                           | Particularly effective at indentifying clusters of data points in high density regions while labeling data points in low-density regions as anomalies or noise. Robust to irregularly shaped clusters/various cluster sized because its based on data density   |
| Gaussian Mixed Models                         | clustering and density estimation, applied to anomaly detection by identifying data points with low likelihoods under the modeled distribution   |
| Autoencoders                         | Consists of an encoder and decoder network to learn compact representation of input data. Anomalies can be detected by comparing the reconstruction error (difference between input and output) of the autoencoder. When the model encounters data that significantly deviates from the learned patterns, the reconstruction error tends to be high, indicating an anomaly|
| Spectral clustering                              | graph based approach that considers data pints with low connectivety to the main cluster as anomalies        |
| Local Outlier Factors (LOF)                      | computes the density of data points relative to their neighbors, data points with significantly lower density than their neighbors are considered anomalies |
| Elliptic Envelope                                | fits a multivariate Gaussian distribution to the data and identifies anomalies based on their Mahalanobis distance from the estimated distribution. VERY useful for detecting multivariate outliers        |
| Histogram Based Outlier Detection                | discretizes the feature space into a histogram and calculates the anomaly scorfe based on the sparsity of histograms. Efficient and good for high-dimensional data        |
