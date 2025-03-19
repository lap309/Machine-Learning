import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM

# Initialize and fit the One-Class SVM model
svm = OneClassSVM(nu=0.05, kernel="rbf")  # Adjust the nu parameter as needed
svm.fit(data)

# Predict whether each data point is an anomaly (-1 for anomalies, 1 for normal data)
predictions = svm.predict(data)

# Visualize the results
def plot_anomaly_detection_results(predictions, title):
    plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
    plt.colorbar(label="Anomaly Score")
    plt.title(title)
    plt.show()

plot_anomaly_detection_results(predictions, "Anomaly Detection using One Class SVM")



# Identify anomalies (outliers)
anomalies_indices = np.where(predictions == -1)[0]
print("Detected anomalies:", anomalies_indices)
