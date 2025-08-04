# Anomaly Detection
-------------------------------------------------
__NOTES__: <br>
__Classification - Supervised and Unsupervised__ <br>
__Highly prone to unbalanced data and gernerally time sensitive (real time scoring or api)__ <br>
__Consider recall as a metric (as opposed to accuracy)__

------------------------------------------------- 

Anomaly detection is about finding patterns of interest or small differences (outliers, exceptions, pecuiliarities) in the data that deviates from expected behavior and would otherwise go undetected. Another similar procedure is noise removal which can be very distracting in the training data for machine learning models. Both noise and anomalies can deter the model and negatively affect model performance <br>

__Inliers: "normal" data points that should represent the majority__ <br>
__Outliers: rare observations that differ statistically (by features or values)__ <br>
<br>
Having adaptability in your anomaly detection is crucial since most data is prone to changing over time. And while this process is concluded statistically, the final determination is often decided by an observer/human reader

<p align=center>Types of Anomalies</p>

| Type   | Description| Example    | Common Methods |
| ---------------------------------- | ------- | ------- | ------|
| Point Anomalies                    | single anomalous value or instance within a larger dataset | Ex: 60 degrees Celsius would be an anomaly | Statistical Methods|
| Contextual (conditional) anomalies | values that are considered anomalies in a certain context  | Ex: 25 degrees Celsius would not be an anomaly in the summer, but it would be an anomaly in the winter. The context here is time/seasonality that determines the analogous status of the value | |
| Collective/Cascading anomalies               | when values are only considered anomalies when considered with another value in the same or another dataset. A set of data instance. Similar to contextual anomalies, but this is dependent on data alone| Ex: If condition1 in the data is met, and then the temperature is 60 degrees, then it would be an anomaly| |

# Methodologies
| Technique   | Common Methods| Best For| Challenges | Notes |
| ---------------------------------- | ------- | ------- | ------- | ------- |
| Statistical Methods                  |Z-score, IQR, Grubb's test| Point Anomalies, simple, small data sets |Sensitive to data assumptions and skewed data. Not robust for contextual or collective anomalies | Consider standardization|
| Supervised Machine Learning | Isolation Forest, SVM, LOF | Divers anomalies| Requires labaled data | |
| UnSupervised Machine Learning | Clustering| When data is unlabeled/anomalies are not pre-defined. Ideal for situations where anomalies are rare or unknown in advance, or detecting for unusual behavior. Additionally good for experimenting and exploring with labeled data to see what the computer identifies| | Not subject to follow contextual use cases| |
| Deep Learning Methods| Autoencoders, LSTM networks, Neural Networks| Complex patterns, big data, time series| Computationally intensive| |


All types of models can be used with anomaly detection but you need to understand the business use case because what qualities as an anomaly and the subsequent process of detection will vastly vary based on the goal and application. <br>
The nature of the data, the problem at hand, and the goals of the project are all things to consider before building a solution, making it hard to have a “universal” approach to anomaly detection. 

* Supervised - anomalies are labeled/known in the dataset
* Unsupervised - anomaly process is not established and anomalies are not known
* Semi-Supervised

# Value/ Business Use Case
Understanding what causes these anomalies or why they occur, in order to prevent in future cases <br>

Company/Business:
-	preventing equipment damage therefore saving money
-	identifying fraudulent transactions
-	Cache Timing, what causes certain log requests to fail and other to load
-	Network traffic
-	Sensor data
  
Sales: 
-	to detect or predict slight changes in customer behavior that may result in a shift in selling, marketing strategy, or development. Allowing them to stay ahead of trends
earlier detection on diagnoses or easier treatment

Manufacturing, Industry: 
-	predictive maintenance
  
Healthcare:
-	health condition monitoring
-	clinical data/survey data
-	seizure, tumor, etc. detection with image detection

Finance/Insurance:
-	fraud detection (in the case of fraudulent transactions, people are often deliberately trying to product inputs that mimic real data). Learning and adapting to identifying this fraud can be crucial for the company. Common method is isolation forest since single transactions may deviate in amount of frequency, making them easily identifiable by partitioning
-	stock market analysis
-	early detection of insider tracking

Public Sector: 
-	detection of unusual images from surveillance
  
Retail:
- sales


# Steps to Building the Solution
1.	Understand the Use Case and the Business Goals
    1. Define and continually refine what constitutes an anomaly. It might constantly change, which means continual re-evaluation.
    2. Define goals and parameters for the project overall. For example, the end goal is probably not just to detect anomalies, but something larger that impacts the business, like block fraudulent charges, cure more patients by detecting health conditions earlier, increase revenue by anticipating future trends, etc. Having larger goals will allow you to better define the scope of the project and the expected output.
    3. Determine, once an anomaly is detected, what the system will do next. For example, send anomalies to another team for further analysis and review, automatic actions on an associated asset/account, etc.
    4. Develop a plan to monitor and evaluate the success of the system going forward.
    5. Identify what anomaly detection frequency (real time vs. batch) is appropriate for the business and the use case at hand.
2.	Get your data
3.	Explore, Clean, and Enrich Data
<br>This step in particular is very important for anomaly detection because often the data contains noise (usually errors, human and computer made) which tend to be similar to the actual anomalies. It is integral to have a deep understanding of what constitutes the difference between anomalies and non-anomalies if you have labeled data available
4.	Build the model
5.	Visualize and Monitor
<br>Visualizations are underrated in anomaly detection but can prove to be a good tool in testing anomaly detection because sometimes they are the clearest way to see outliers, especially in large datasets
6.	Deploy with real world data
<br>In many cases, anomaly detection needs to be scored in real time as it is generally time sensitive

