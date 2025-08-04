# Unsupervised Anomaly Detection
Data is not labeled, and therefore unsupervised can handle more complex data sets <br>


<ins> Novelty Detection: </ins> the training set does NOT have outliers and is made exclusively of inliers so that the algorithm learns the concept of “normality”. The test set is provided to the model and we want to know if observations in the test set have the same distribution as the train set, using the distribution results to inform us if there are outliers in the test dataset or not


<ins>Outlier Detection: </ins>The training set contains outliers and it is assumed that the number of outliers is small enough in proportion that the model will be able to indicate the difference between outlier and normal behavior



| Common Models                                    | Description| Best for| Challenges |
| -------------------------------------------------| -----------| --------| -----------|
| * Isolation Forest                                 | ensemble method that isolates anomalies by constructing random forests and isolating data points that require fewer splits in the trees to be isolated. Less effective for contextual anomalies | | |
| * Local outlier factor (LOF)                     | Calculates the density of data around a point and compares it to its neighboring data points to determine how isolated the point is relative to it's surroundings. Similar to KNN but uses the points that are furtherst apart to draw conclusions whereass KNN makes assumptions based on data points that are closest together. If a point's density is significantly lower than its neighbors, it is marked as an anomaly  | Non-linear data and complex data sets. Good to detect unusual activity or patterns in logs | Computationally expensive |
| * K means Clustering                               | treats data points in small clusters as anomalies | | |
| * Hierarchal Clustering                            | treats data points in small clusters as anomalies | | |
| Isolation Kernel (iKernel)                       | an extension of Isolation Forest that uses kernel methods to capture non-linear relationships in data   | | |
| * One Class Support Vector Machines                | constructs a hyperplane that separates the majority of the data from potential anomalies. VERY useful when anomalies are rare and not well distributed | | |
| DBSCAN                                           | Particularly effective at indentifying clusters of data points in high density regions while labeling data points in low-density regions as anomalies or noise. Robust to irregularly shaped clusters/various cluster sized because its based on data density   | | |
| Gaussian Mixed Models                         | clustering and density estimation, applied to anomaly detection by identifying data points with low likelihoods under the modeled distribution   | | |
| Autoencoders                         | Consists of an encoder and decoder network to learn compact representation of input data by compressing input data into a smaller representation and then reconstructing the original data from this compressed version. Anomalies can be detected by comparing the reconstruction error (difference between input and output) of the autoencoder. When an autoencoder can't accurately reconstruct a point because it's too different from the training data or significantly deviates from the learned pattern, the reconstruction error tends to be high, indicating an anomaly| High dimensional data (images or logs) for example  identifying defective products on assembly lines by comparing to  "normal" images| Require large training sets to perform well. May require more hyperparameter tuning to avoid overfitting|
| Spectral clustering                              | graph based approach that considers data pints with low connectivety to the main cluster as anomalies        | | |
| Elliptic Envelope                                | fits a multivariate Gaussian distribution to the data and identifies anomalies based on their Mahalanobis distance from the estimated distribution. VERY useful for detecting multivariate outliers        | | |
| Histogram Based Outlier Detection                | discretizes the feature space into a histogram and calculates the anomaly scorfe based on the sparsity of histograms. Efficient and good for high-dimensional data   | |    |
| (LSTM)Long Short-Term_Memory                     | Processes sequential data and recognizes temporal relationships| Time Series data. Popular use cases are finanical forecasting to detect unusual spikes or dips in stock prices, or to monitor sensor readings over time to predict potential failures in conncted devices| Computationally intensive and requires careful tuning to avoid vanishing or exploding graients|
