import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from keras.models import Sequential
from keras.layers import Dense

# Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Neural Network for Anomaly Detection
nn_model = Sequential()
nn_model.add(Dense(8, input_dim=2, activation='relu'))
nn_model.add(Dense(1, activation='sigmoid'))
nn_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
nn_model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=0)
train_pred = nn_model.predict(X_train)
train_pred = (y_nn_pred > 0.5).astype(int)

print("Confusion Matrix:", confusion_matrix(y_train, train_pred))
print("Classification Report:", classification_report(y_train, train_pred))

test_pred = nn_model.predict(X_test)
print("Confusion Matrix:", confusion_matrix(y_test, test_pred))
print("Classification Report:", classification_report(y_test, test_pred))

# Visualization of Results (for Neural Network)
plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1], c='b', label='Normal Data')
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1], c='r', label='Anomalies')
plt.title('Neural Network Anomaly Detection')
plt.legend()
plt.show()


