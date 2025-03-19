import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Initialize and fit the KNN model
k = 5  # Adjust the number of neighbors as needed
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(data, labels)

# Predict whether each data point is an anomaly (0 for anomalies, 1 for normal data)
predictions = clf.predict(data)

# Visualize the results
plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
plt.colorbar(label="Anomaly Score")
plt.title("Anomaly Detection using KNN")
plt.show()

# Identify anomalies (outliers)
anomalies_indices = np.where(predictions == 0)[0]
print("Detected anomalies:", anomalies_indices)
