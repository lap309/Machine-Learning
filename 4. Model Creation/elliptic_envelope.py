import numpy as np
import matplotlib.pyplot as plt
from sklearn.covariance import EllipticEnvelope


# Elliptic Envelope
elliptic = EllipticEnvelope(contamination=0.05)
labels_elliptic = elliptic.fit_predict(X)
axs[1, 1].scatter(X[:, 0], X[:, 1], c=labels_elliptic, cmap='viridis')
axs[1, 1].set_title("Elliptic Envelope")
plt.show()
