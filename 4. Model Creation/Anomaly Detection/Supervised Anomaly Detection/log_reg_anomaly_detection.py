import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Logistic Regression for Anomaly Detection
lr = LogisticRegression()
lr.fit(X_train, y_train)
train_pred = lr.predict(X_train)

print("Confusion Matrix:",confusion_matrix(y_train, train_pred))
print("Classification Report:",classification_report(y_train, train_pred))

test_pred = lr.predict(X_test)

print("Confusion Matrix:",confusion_matrix(y_test, test_pred))
print("Classification Report:",classification_report(y_test, test_pred))
