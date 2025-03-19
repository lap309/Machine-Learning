import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM

# Initialize and fit the One-Class SVM model
clf = OneClassSVM(nu=0.05, kernel="rbf")  # Adjust the nu parameter as needed
clf.fit(data)

# Predict whether each data point is an anomaly (-1 for anomalies, 1 for normal data)
predictions = clf.predict(data)

# Visualize the results
plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
plt.colorbar(label="Anomaly Score")
plt.title("Anomaly Detection using One-Class SVM")
plt.show()

# Identify anomalies (outliers)
anomalies_indices = np.where(predictions == -1)[0]
print("Detected anomalies:", anomalies_indices)
