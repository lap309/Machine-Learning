
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Naive Bayes for Anomaly Detection
nb = GaussianNB()
nb.fit(X_train, y_train)
train_pred = nb.predict(X_train)

print("Train Confusion Matrix: \n", confusion_matrix(y_train, train_pred))
print("Train Classification Report:\n", classification_report(y_train, train_pred))


#Apply to test set
test_pred = nb.predict(X_test)

# Evaluate the test set
print("Test Confusion Matrix: \n", confusion_matrix(y_test, test_pred))
print("Test Classification Report:\n", classification_report(y_test, test_pred))
