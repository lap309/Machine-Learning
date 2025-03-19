import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor


# Local Outlier Factor (LOF)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
labels_lof = lof.fit_predict(X)
axs[0, 2].scatter(X[:, 0], X[:, 1], c=labels_lof, cmap='viridis')
axs[0, 2].set_title("Local Outlier Factor")
