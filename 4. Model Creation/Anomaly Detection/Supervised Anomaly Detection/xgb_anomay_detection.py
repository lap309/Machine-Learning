import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from xgboost import XGBClassifier

# Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# XGBoost for Anomaly Detection
xgb = XGBClassifier()
xgb.fit(X_train, y_train)
train_pred = xgb.predict(X_train)

