# Churn Prediction (Attrition)
In it's simplest form, churn/attrition is when customers leave and stop buying your product, using your service, or leave your company <br>
For most businesses, customer churn is a critical metric because it is much less expensive to retain existing customers than it is to acquire new customers. <br>
To detect early signs fo potential churn, we first develop a holistic view of the customers and their interactions, then build predictive models to accurately predict churn and then companies take action by building targeted marketing campaigns around preventing it or by making product changes to combat churn.
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
- Increasing and reraining current customers (retention strategy)

### Industries that monitor Churn
Most industries that rely on subscriptions, customer/buyers will be interested in monitoring churn. This spans across several industries, some examples listed below:
- streaming services, entertainment
- digital media/marketing
- consumer goods and retail
- energy/utilities
- telecom/wireless
- B2C services

### Define Churn and Customers: Things to Consider
- How are we defining a "user"? For example, is someone who uses the product/service only once then enver again going to be considered churn? What if they buy a product, then don't buy anything for 9 months, then buy again? Are they a new customer or a returning customer?
  <br> ex: a user who hasn't taken any actino on the website in 4 months
- A churn period that is too long risks predictive models with low churn rates and reduces performance. A churn period that is too short makes it difficult for the business to take action or gather enough data on churn causes.
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
_The more resources the better for the  model to detect patterns_ <br>
- subscription information (products customers have bought, activation and cancellation dates, add ons)
- payment information (how much they pay, method of payment)
- product usage information (login information, clicks, minutes of interaction)
- interaction information (chats or calls made by clients, rating on support services, claim details)

### Clean Data and Enrich
- Understand all your values and make contextual decision about what data to keep
- Decide what to do with Missing Data (drop or re-assign values)
- If you are considering calculations and the churn definition is time based, then make sure to do rolling calculations or calculations over a time period instead of total all-time purchases

### Splitting the Data
In most cases, a time-based split will be the optimal choice. It's not recommended to use a random split as this will cause overfitting and will not allow churn predictions to be generalized to the future

### Common Visualizations
- The evolution of churn over time and targeted churners
- Which product features have an impact on churn
- Descriptive statistics of those key features for easy reference or visual simulations illustrating how changing features would impact churn probability
- Additonal insights about the chosen churn model
- churn rates by location
- Churn rates by all features in the data

### Building a Model
Train and Test Set: If you have defined a churn period of 4 months, and you have labeled data up until April 2025. Then you will want your train dataset to be up until Sept 2024, your validation set to be Sept 2024-Jan 2025, and Jan-Apr 2025 as the test set. Any data after that can be used in production.

One of the common pitfalls for a churn model is training your  model on both past qand future events. To avoid this common mistake, answer the question: <br>
When your model is in production, what data will be available to you? <br>
When would you like your prediction to be: next week? Next month?<br>
This should be the only data included in the train set <br>
<br>
When you begin modeling, start off small. Little by little, continue to add features and evaluate their effect on the accuracy of the model. Complex models will not always be the answer, instead focus on optimizing the right features and running simpler models.
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

### Post Analysis
Are there any patterns of churn by common demographics? (Age, Gender, Location, service type, etc.) <br>
Is there a specific season where we saw higher churn rates?

### Next Steps - what to do after you build the model?
Now that I know who is likely to churn, now what? <br>
Many business infer that theose who scored the highest (i.e are most likely to churn) should be the ones to target. While the ideology is there, there are additional things to consider before finalizing the list of people to target for future marketing campaigns. <br>
You could lump all the people likely to churn into an audience to target with a marketing campaign, but realisitcall,y not every single customer who churns will come back. Some customers are lost causes and we don't want to spend money on those profiles. To save time and resources, you can go one step further and use **uplift modeling** and **client clustering** to drive return on investment (ROI), essentially spending time and resources targesting churners who will respond positively to your campaign. <br>
Uplift models look to optimzie the effects of marketing campaigns by predicting which customers are likely to take the desired action. They score customers into one of the following groups to maximize results and minimize wasted moeny and effort.<br>
In the cart below, only Persuadables (along with randomized control group) would be targeted. We don't want to target lost causes, and sure thing customers would take action whether we market to them or not, so we can save our money. We want to target the persuadables sub-group.<br>

|         |       +     |      -   |
|---------|-------------|----------|
|     +   | **Sure Things** <br> Those that would react positively either way and thus represent wasted marketing costs  | **Do Not Disturbs** <br> those who would have had a positive responce if they didn't receive any marketing, but after marketing react negatively and thus should not be targeted|
|     -   | **Persuadables** <br>(__who we want to target__) those that would have had a negative response byt are then positively persuaded by marketing | **Lost causes**  those who will have a negative response with or without marketing and thus represent wasted marketing costs|


https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/comments
