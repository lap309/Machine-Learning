# Churn Prediction (Attrition)
In it's simplest form, churn/attrition is when customers leave and stop buying your product, using your service, or leave your company <br>
Predictive models are built to accurately predict churn and then companies take action by building targeted marketing campaigns around preventing it or by making product changes to combat churn.
<br>
Quick Notes: Classification Model or Clustering Model <br>
It's a good idea to start with unsupervised clustering even if you have labeled data. This will find relevant features that are most relevant to your churn calculations. <br>
Classification models will give a churn score to determine how likely specific customers are to leave. Churn scores enable you to build rules together to define your customer segments

### Types of Churn
* Subscription Churn : when users/consumers are on contract for a set period of time (monthly subscriptions, work contract, etc.) and consuemrs decide not to come back after that period is over. This is easier to define, predict, and prevent since there's a clear defined window where churn is a risk and this period can be marketed on. <br>
In this case, a customer churns when they request cancellation of their subscription, but this is always clearly stated by the customer
* Non-subscription Churn: when users/consumers can end their relationship with the business at any time, they come and go at will. Signs of churn are harder to measure in this instance because indicators of churn are contextually dependent on the situation. For example, indicators of churn could be when user activity gradually declines or they could just stop their business all of a sudden. These are harder to define wince it is not pre-determined when a customer could start their churn period. <br>
Determining churn requires analyzing your customer's behavioral tendencies in order to predict churn possibility for unsupervised learning. Supervised learning requires several internal teams getting together and determining how they want to define churn periods.
<br>
These are more contextual cases and will depend on the specific business organization and how they are measuring or defining churn.
* Mix of subscription and non-subscription churn

#### Actions from Churn Prediction
- Predicting who will or will not churn
- ML for causation, develop a model to understand the reasons causing the churn. This allows clients to attack the root cause of what's causing the churn and reduce it
- Marketing campaigns to re-engage likely churners
- Uncover potential deeper drivers of churn that can be addressed long term
- Increasing and retraining current customers

### Define Churn: Things to Consider
- How are we defining a "user"? For example, is someone who uses the product/service only once then enver again going to be considered churn? What if they buy a product, then don't buy anything for 9 months, then buy again? Are they a new customer or a returning customer?
- Is there some minimal threshold after which a user should be considered and included in churn analysis? hwat is the time period/time frame?
- Do we want to perform segmentation based on their behavior? Which customers do we care about? churn reduction campaigns should be targeted towards a well defined customer segment
- How are we defining churn? When do we consider a consumer lost? When do we consider a customer at risk?
- Do we have a defined churn period? How would we identify that in the data?
- When is the optimal time in a customer's life cycle to try to re-engage them?
- What is this churn prediction going to be used for? Once we predict churn, what actions will we take next?
<br>
When defining churn, it may be possible that the definition needs to be adjusted or tweaked during the course of the project depending on your findings.

### Necessary Data
*Customer Identifier <br>
*A date/time of that customer's last interaction <br>
(Optional) static demographic inforamtion about users or types of user actions. <br>
_The more resources the better for the  model to detect patterns_

### Clean Data and Enrish
- Understand all your values and make contextual decision about what data to keep
- Missing Data

### Common Visualizations
- The evolution of churn over time and targeted churners
- Which product features have an impact on churn
- Descriptive statistics of those key features for easy reference or visual simulations illustrating how changing features would impact churn probability
- Additonal insights about the chosen churn model
- Churn rates by all features in the data

### Building a Model
One of the common pitfalls for a churn model is training your  model on both past qand future events. To avoid this common mistake, answer the question: <br>
When your model is in production, what data will be available to you? <br>
This should be the only data included in the train set <br>
<br>
Another common pitfall is perceiving the model as a one shot study. You won't do much with a single iteration of a customer churn prediction model and you risk overlooking critical aspects in the project such as scalability and reproducibility. Multiple iterations help uyou create a successful scalable and long-term strategy to retain and increase customer loyalty. <br>
<br>
#### Models
Supervised <br>
Random Forest <br>
Logistic Regression <br>
K Nearest Neighbors <br>
SVM <br>

### Optimizing
When you first start working on the model, focus on optimizing for the right features and running simpler models. Once you know you have the best features, you can optimize and find the best model. This will save time and resources in the long run. <br><br>
Decide what you are measuring and what you want to optimize towards. Make sure you choose an evaluation metric that aligns with the business goals.
