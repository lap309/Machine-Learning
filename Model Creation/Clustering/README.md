# Clustering
Unsupervised technique where datapoints that are similar are grouped to each other to identify patterns in data

#### Applications of Clustering
- Looking for trends in data
- Data compression, all data clustering around a point can be reduced to just that point. For ex, reducing color depth of an image
- Pattern Recognition

**K-means Clustering**: Attempts to identify the center of each cluster by minimizing the distance between the center and all points in the cluster. Must be told how many clusters to look for.

_Limitations_: 
- Requires number of clusters to be known in advance
              
- Requires linear custer boundaries
              
- Struggles when clusters have irregular shapes
              
- Will always produce an answer finding the required # of clusters even if the data isn't clustered or clustered in that many clusters
                      

**Spectral Clustering**: Attempts to overcome the linear boundary of K-means and clusters by graphically partitioning the data. It looks for nodes in a graph with a small distance between them.
