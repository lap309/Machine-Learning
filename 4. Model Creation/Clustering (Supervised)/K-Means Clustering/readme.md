# K-Means Clustering
DATA SHOULD BE `SCALED` (because everything is being applied based off of distance and location) unless you are purposely weighing one variable more than the rest. Although this is not as common
Looking at how similar new data is to our labeled/known data <Br>
The assumption that (geographically) similar points will most likely have similar outcomes
To decide a label for each new data point, taking into consideration what the labels of the surrounding data points are k nearest neighbors away  <br>
ex: deciding someone's political standing by looking at the political standing of their household (small k) vs. their neighborhood or town's political standing (larger k) <br><Br>

Using neighbored labels as an indicator, it is simple to use k-means clustering with `multiple class models`



### Choosing k (hyperparameter)
k = 1 --> leads to overfitting
k = n_samples --> leads to underfitting. Will classify every single datapoint as the majority vote of the dataset

#### Elbow Method Approach
Looks at the error rate for each k-value for the dataset. <br>
You want to choose the k value right before theres a sharp curve/right angle to the right

To avoid having a tie, one neighbor is positive, one is negative, it is suggested to choose a k such that  k= n_labels + 1 <br>
ex: 2 classes --> k=(2+1)<br>
3 classes --> k=(3+1) <br>
4 classes --> k=(4+1) etc..... <br><Br>

Other options include: <br>
- weighint the points according to their distance from the point
- randomly choosing an outcome

### Choosing the Distance Methodology: how to measure the distance between each of our neighbors?
#### Euclidiean Distance (L2)
The linear distance that follows the pathagorean theoream
$$distance = \sqrt{(\Delta{x)^2} + (\Delta{y)^2}} $$

#### Manhattan Distance (L1)
analogous to having to walk on the sidewalk in the city, can only move in straight lines (left/right or up/down)
$$distance = |\Delta{x}|+ |\Delta{y}| $$

## K-Means Clustering for Regression
Works similarly to Clustering but the value predicted is the mean value of its neighbors, and the k value will indicate how many neighbors next to the data point to include in a rolling average to predict the values<br>
So when K is the same value as the number of points, a single value is predicted, that is the mean of all the values will be predicted.<Br>
For K >1,  KNN regression acts as a smoothing function with just the rolling average of the closest k points <br>
For K = 1, the prediction simply connects each one of the points exactly. We're just saying the nearest neighbor for each one of the points is going to be our prediction.

### Pros and Cons of K-Means Cluster
__Pros:__
* Simple to implement
* Adapts to new data well
* highly interpretable

__Cons:__
* slow to predict because of the many distance calculations
* does not output a clear equation with feature importance or causal inference
  - does not generate a proess to udnerstand how we can generate certain labels
* may require a lot of memory. the model uses all the values in the training set every time to fit the model
* the model gets complicated as we increase the number of features/variables
