import numpy as np
import tensorflow as tf
from tensorflow import keras

# Generate a synthetic dataset with anomalies
np.random.seed(42)
normal_data = np.random.randn(300, 10)
anomalies = 4 + 1.5 * np.random.randn(10, 10)  # Generating anomalies far from normal data

# Combine normal and anomaly data
data = np.vstack([normal_data, anomalies])

# Build an autoencoder model
input_dim = data.shape[1]
encoding_dim = 5  # Adjust the bottleneck layer size as needed

model = keras.Sequential([
    keras.layers.Input(shape=(input_dim,)),
    keras.layers.Dense(encoding_dim, activation='relu'),
    keras.layers.Dense(input_dim, activation='linear')  # Linear activation for reconstruction
])

model.compile(optimizer='adam', loss='mse')

# Train the autoencoder
model.fit(data, data, epochs=100, batch_size=32, shuffle=True)

# Calculate reconstruction errors
reconstructed_data = model.predict(data)
reconstruction_errors = np.mean(np.square(data - reconstructed_data), axis=1)

# Set a threshold for anomaly detection (e.g., using a percentile)
threshold = np.percentile(reconstruction_errors, 95)  # Adjust the percentile as needed

# Identify anomalies based on the threshold
anomalies_indices = np.where(reconstruction_errors > threshold)[0]
print("Detected anomalies:", anomalies_indices)
