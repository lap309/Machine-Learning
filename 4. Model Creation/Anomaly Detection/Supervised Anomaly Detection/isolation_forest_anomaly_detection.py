import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize and fit Isolation Forest for training anomaly detection
iso_forest = IsolationForest(contamination=0.05, random_state=42)
iso_forest.fit(X_train)
train_pred = iso_forest.predict(X_train)

print("Confusion Matrix: \n", confusion_matrix(y_train, train_pred))
print("Classification Report:\n", classification_report(y_train, train_pred))


#Apply to test set
test_pred = iso_forest.predict(X_test)

# Evaluate the test set
print("Confusion Matrix: \n", confusion_matrix(y_test, test_pred))
print("Classification Report:\n", classification_report(y_test, test_pred))

# Visualize the results
def plot_anomaly_detection_results(predictions, title):
    plt.scatter(data[:, 0], data[:, 1], c=predictions, cmap='viridis')
    plt.colorbar(label="Anomaly Score")
    plt.title(title)
    plt.show()

plot_anomaly_detection_results(test_predictions, "Anomaly Detection using Isolation Forest")




