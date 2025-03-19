import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier

# Initialize and fit AdaBoost classifier for anomaly detection
ada = AdaBoostClassifier(n_estimators=100, random_state=42)
ada.fit(data, labels)
ada_predictions = ada.predict(data)

# Visualize the results
def plot_anomaly_detection_results(predictions, title):
    plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
    plt.colorbar(label="Anomaly Score")
    plt.title(title)
    plt.show()

plot_anomaly_detection_results(ada_predictions, "Anomaly Detection using AdaBoost")
