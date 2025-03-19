from sklean.cluster import SpectralClustering

model = SpectralClustering( n_clusters = 1 ,affinity ='nearest_neighbors', assign_labels = 'kmeans')
labels = model.fit_predict(data)
plt.scatter(circles[:, 0], circles[:, 1], s=15, linewidth=0, c=labels, cmap='flag')
plt.show()


######## Anomaly Detection ##########
# Spectral Clustering
spectral = SpectralClustering(n_clusters=1, affinity="nearest_neighbors")
spectral.fit(X)
labels_spectral = spectral.labels_
axs[0, 0].scatter(X[:, 0], X[:, 1], c=labels_spectral, cmap='viridis')
axs[0, 0].set_title("Spectral Clustering")

