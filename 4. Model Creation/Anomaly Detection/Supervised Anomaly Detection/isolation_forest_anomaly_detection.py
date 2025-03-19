import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Initialize and fit Isolation Forest for anomaly detection
iso_forest = IsolationForest(contamination=0.05, random_state=42)
iso_forest.fit(data)
iso_forest_predictions = iso_forest.predict(data)

# Visualize the results
def plot_anomaly_detection_results(predictions, title):
    plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
    plt.colorbar(label="Anomaly Score")
    plt.title(title)
    plt.show()

plot_anomaly_detection_results(dt_predictions, "Anomaly Detection using Decision Trees")

