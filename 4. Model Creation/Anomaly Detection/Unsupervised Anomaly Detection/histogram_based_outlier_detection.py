import numpy as np
import matplotlib.pyplot as plt
from pyod.models.hbos import HBOS

# HBOS (Histogram-Based Outlier Detection)
hbos = HBOS(contamination=0.05)
labels_hbos = hbos.fit_predict(X)
axs[1, 2].scatter(X[:, 0], X[:, 1], c=labels_hbos, cmap='viridis')
axs[1, 2].set_title("HBOS")
plt.show()

