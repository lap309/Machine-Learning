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

|    | |     |
| ---------------------------------- | ------- | ------- |
| Point Anomalies                    | single anomalous value or instance within a larger dataset | Ex: 60 degrees Celsius would be an anomaly |
| Contextual (conditional) anomalies | values that are considered anomalies in a certain context  | Ex: 25 degrees Celsius would not be an anomaly in the summer, but it would be an anomaly in the winter. The context here is time/seasonality that determines the analogous status of the value |
| Collective anomalies               | when values are only considered anomalies when considered with another value in the same or another dataset. A set of data instance. Similar to contextual anomalies, but this is dependent on data alone| |

# Models

All types of models can be used with anomaly detection but you need to understand the business use case because what qualities as an anomaly and the subsequent process of detection will vastly vary based on the goal and application. <br>
The nature of the data, the problem at hand, and the goals of the project are all things to consider before building a solution, making it hard to have a “universal” approach to anomaly detection. 

* Supervised
* Unsupervised
* Semi-Supervised

# Value/ Business Use Case
Understanding what causes these anomalies or why they occur, in order to prevent in future cases <br>

Company/Business:
-	preventing equipment damage therefore saving money
-	identifying fraudulent transactions
  
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
-	fraud detection (in the case of fraudulent transactions, people are often deliberately trying to product inputs that mimic real data. Learning and adapting to Identifying this fraud can be crucial for the company
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

