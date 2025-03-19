import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier

# Initialize and fit Gradient Boosting classifier for anomaly detection
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb.fit(data, labels)
gb_predictions = gb.predict(data)

# Visualize the results
def plot_anomaly_detection_results(predictions, title):
    plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
    plt.colorbar(label="Anomaly Score")
    plt.title(title)
    plt.show()

plot_anomaly_detection_results(gb_predictions, "Anomaly Detection using Gradient Boosting")
