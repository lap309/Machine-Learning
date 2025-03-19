import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Initialize and fit Extreme Value Theory (EVT) for anomaly detection
mu, sigma = norm.fit(data)  # Estimate distribution parameters
threshold = np.percentile(norm.pdf(data, mu, sigma), 95)  # Set a threshold
evt_predictions = (norm.pdf(data, mu, sigma) < threshold).astype(int)
