# Clustering
Unsupervised technique where datapoints that are similar are grouped to each other to identify patterns in data (but the answer is not known) <Br>
<br>
Because the answer is not known in clustering problems, there is no answer guide or target output to compare the model results with.As such, the concept of overfitting does not apply to unsupervised learning and there is no need to perform a train/validation/test split nor to apply cross-validation. <br>
<br>
The full dataset can be input into the model, but it may still need to be scaled!!!

#### Applications of Clustering
- Looking for trends in data
- Data compression, all data clustering around a point can be reduced to just that point. For ex, reducing color depth of an image
- Pattern Recognition

**K-means Clustering**: Attempts to identify the center of each cluster by minimizing the distance between the center and all points in the cluster. Must be told how many clusters to look for.

_Limitations_: 
- Requires number of clusters to be known in advance
              
- Requires linear custer boundaries
              
- Struggles when clusters have irregular shapesor when one cluster exists within another (concentric circleS)
              
- Will always produce an answer finding the required # of clusters even if the data isn't clustered or clustered in that many clusters
                      

**Spectral Clustering**: Attempts to overcome the linear boundary of K-means and clusters by graphically partitioning the data. It looks for nodes in a graph with a small distance between them.

_Limitations_:
- Slower than K-means

  ** DBSCAN (Density Based Spatial Clsutering of Applications with Noise)
