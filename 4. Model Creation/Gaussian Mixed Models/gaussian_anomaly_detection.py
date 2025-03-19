import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Generate a synthetic dataset with anomalies
np.random.seed(42)
normal_data = np.random.randn(300, 2)
anomalies = 4 + 1.5 * np.random.randn(10, 2)  # Generating anomalies far from normal data

# Combine normal and anomaly data
data = np.vstack([normal_data, anomalies])

# Train a Gaussian Mixture Model (GMM)
n_components = 5  # Number of Gaussian components
gmm = GaussianMixture(n_components=n_components, covariance_type='full', random_state=42)
gmm.fit(data)

# Calculate the likelihood scores for each data point
likelihoods = -gmm.score_samples(data)

# Set a threshold for anomaly detection (e.g., using a percentile)
threshold = np.percentile(likelihoods, 95)  # Adjust the percentile as needed

# Identify anomalies based on the threshold
anomalies_indices = np.where(likelihoods < threshold)[0]

# Plot the data and highlight anomalies
plt.scatter(data[:, 0], data[:, 1], c='b', label='Normal Data')
plt.scatter(data[anomalies_indices, 0], data[anomalies_indices, 1], c='r', marker='x', label='Anomalies')
plt.legend()
plt.title('Anomaly Detection using Gaussian Mixture Model')
plt.show()
