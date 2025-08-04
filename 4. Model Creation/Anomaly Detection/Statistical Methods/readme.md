# Statistical Methods - Anomaly Detection

The most foundational but still strong options as the root base for other anomaly detection options. <br>
Not reliable for skewed datasets (prone to false positives) and they are not robust for detecting contextual nor collective anomalies


### Methodologies
* **Z-score:** Measures how many standard deviations a data point is from the mean (consider normalization if comparing several features) <br>
* **Interquartile Range (IQR):** Identifies outliers by calculating the spread of the middle 50% of the data <br>
* **Grubb's Test:** Detects single outliers in normally distributed data <br>
