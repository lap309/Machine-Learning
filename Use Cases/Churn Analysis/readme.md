# Churn Prediction (Attrition)
In it's simplest form, churn/attrition is when customers leave. <br>
Predictive models are built to accurately predict churn and then companies take action by building targeted marketing campaigns around preventing ir or by making product changes to combat churn.
<br>


### Types of Churn
* Subscription Churn : when users/consumers are on contract for a set period of time (monthly subscriptions, work contract, etc.) and consuemrs decide not to come back after that period is over. This is easier to define, predict, and prevent since there's a clear defined window where churn is a risk and this period can be marketed on
* Non-subscription Churn: when users/consumers can end their relationship with the business at any time, they come and go at will. Signs of churn are harder to measure in this instance because indicators of churn are contextually dependent on the situation. For example, indicators of churn could be when user activity gradually declines or they could just stop their business all of a sudden. These are harder to define wince it is not pre-determined when a customer could start their churn period.
<br>
These are more contextual cases and will depend on the specific business organization and how they are measuring or defining churn.
* Mix of subscription and non-subscription churn

#### Actions from Churn Prediction
- Marketing campaigns to re-engage likely churners
- Uncover potential deeper drivers of churn that can be addressed long term

### Things to Consider
- How are we defining a "user"? For example, is someone who uses the product/service only once then enver again going to be considered churn? Or is there some minimal threshold after which a user should be considered and included in churn analysis?
- How are we defining churn? When do we consider a consumer lost?
- Do we have a defined churn period? How would we identify that in the data?
- What is this curn prediction going to be used for? Once we predict churn, what actions will we take next?

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
This should be the only data included in the train set

### Optimizing
When you first start working on the model, focus on optimizing for the right features and running simpler models. Once you know you have the best features, you can optimize and find the best model. This will save time and resources in the long run. <br><br>
Decide what you are measuring and what you want to optimize towards. Make sure you choose an evaluation metric that aligns with the business goals.
