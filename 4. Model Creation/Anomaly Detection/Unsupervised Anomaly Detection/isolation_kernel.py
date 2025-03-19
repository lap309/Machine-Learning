import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Isolation Kernel
kernel = KMeans(n_clusters=1, random_state=42)
kernel.fit(X)
labels_kernel, _ = pairwise_distances_argmin_min(X, kernel.cluster_centers_)
axs[1, 0].scatter(X[:, 0], X[:, 1], c=labels_kernel, cmap='viridis')
axs[1, 0].set_title("Isolation Kernel")
plt.show()
