import sklearn.cluster
import matplotlib.pyplot as plt

## the algorith will predict clusters and a cluster center
kmean = sklearn.cluster.KMeans(n_clusters = 4)
kmean.fit(data)
clusters = kmean.predict(data)     #make prediction

## metadata about the cluster centers
centers = kmeans.cluster_centers_
centers

#Evaluate: Find the inertia score
inertia_score = kmeans.inertia_
inertia_score

# plotting the points from the clusters, color coding by cluster, and plotting the centers of each cluster as a red x

plt.scatter(data[:, 0], data[:, 1], size=5, linewidth=0, color =clusters)
for cluster_x, cluster_y in kmean.cluster_centers_:
    plt.scatter(cluster_x, cluster_y, size=100, c='r', marker='x')
plt.show()
