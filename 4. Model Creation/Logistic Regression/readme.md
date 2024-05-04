# Logistic Regression ( Binary Clasifier)
Using the Sigmoid Function, all values or inputs of x will be between 0 and 1,and will represent the probability of the sample being in class 1. The class that x-value is assigned to depends on the determined probability threshold.<br><Br>

Logistic Regression is based off of linear regression, but it takes numerical inputs and outputs a numerical prediction through the use and formula of the Sigmoid Curve. <br><br>

#### How does it work? <br>
We take our familiar linear function...
$$f(X) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_d x_d$$

... and feed it into the sigmoid curve...
$$s(X) = \frac{1}{1+e^{-f(X)}}$$

... to create our final predictive model:
$$s(X) = \frac{1}{1+e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_d x_d)}}$$

Features of the Sigmoid Curve: <Br>
- always produces an output between 0 and 1 (and we interpret this as the probability of class 1 occurring)
- The Sigmoid Curve is smooth and never makes a sharp jump

#### The output
Once we have our model's estimate we can make a decision on which class it belongs to. 

Since $X$ must belong to one of the two classes, we assign it to the class our model believes is more likely. This is to say that we assign it to class $1$ if $s(X) \geq 1-s(X)$, otherwise we assign it to class $0$. 

As an example, let's say we are trying to predict if someone will get hired or not. Getting hired is class 1 and not getting hired is class 0. Our model tells us: 

|    Class  |  0  |  1  | 
| --------- |:---:|:---:|
|Probability|0.73 |0.27 | 

These are called soft predictions. This means that there a 0.73 probability that the person will not get hired and a 0.27 probability that the person will get hired. These two should addup to 1.  

We now have to make the hard prediction of saying if that individual will get hired. Since Class 0 is more likely than Class 1, we can make a decision to predict that the individual will not get hired. 

Equivalently, in a two-class scenario, we can look at the probability of Class 1 happening and predict Class 1 if the probability is larger than 0.5.

### Hypothesis Testing
The P>|z| value is a hypothesis test for every single coefficient for each variable <br>
H0 = the coefficient is zero /this variable has no effect in the model or on the dependent variable <br>
H1 = the coefficient is not zero

if P>|z| < .05, then we have reason to believe the parameter has an effect on the dependent variable and should be kept in the model

### Odds Ratio: Interpreting the Coefficients
When we interpret logistic regression coefficients, coefficients don't represent the **probability** of the dependent outcome, but rather the ODDS RATIO of the dependent outcome. <br>
Odds ratio refers to the ratio between the odds of an outcome happening versus the outcome not happening.
$$\frac{p}{1-p}$$

To calculate the odds ration of the parameters in the logistic regression model, you just take the coefficient from the output and set it to the power of e
$$\text{odds ratio} = e^{2.369} = 10.69 $$

This means that with one unit increase in *x*, the odds of *y* increase by a factor of approx 10.69 <br>
Note: for cases where the odd ratio is less than 1, for example an odds ratio of .976, the odds "increase by a factor of .976" which is to say that the odds actually decrease by $\frac{1}{0.976} \approx 1.025$ <br><Br>
Overall, if the coefficient is **positive**, then that variable makes it **more likely to be occur**. If a coefficient is **negative** then that variable makes it **less likely to occur** <Br><Br>

Another way to interpret the coefficients is to say that a 1% increase in *x* leads to coefficient% increase in *y*

## Multi-class Logistic Regression
Utilizes the technique, 1 vs. all: <br>
ex: class 1, class 2, class 3 <br> <br>

We run a logistic regression of ]:<br>
Class 1 vs. Everything Else (Class 2 and Class 3) to define the decision boundary for Class 1<br>
Class 2 vs. Everything Else (Class 1 and Class 3) to define the decision boundary for Class 2<br>
Class 3 vs. Everything Else (Class 1 and Class 2) to define the decision boundary for Class 3<br><Br>
At the end, we end up with 3 logistic models splitting out their own probability. <br>
Then you take the value you want to predit, then plug that in to all 3 equations and get the probability that x is in class 1, the probability that x is in class 2, and the probability that x is in class 3.<br>

Imagine we have 3 classes. We build a classifier (logistic regression, in this case) for each class. We get a probability of being in each class vs being in any other class. For a certain data point, this look like: 

<table>
<tr> </tr> <tr> </tr> <tr> </tr>
<tr><td>

|    Class  |  $s_1$  |       
| --------- |:---:|
|0 |0.5 |
|1 or 2 |0.5 |
| | |

</td><td>

|    Class  |  $s_2$  |
| --------- |:---:|
|1 |0.7 |
|0 or 2 |0.3 |
| | |

</td><td>
We take the probability that is the highest and assign x to that class as the prediction.<br>
In this case, if we look at the probabilities for class 0,1,2, the maximum is 0.7 for class 1. Thus, this data point would belong to class 1 from the logistic regression model<br> <br>

NOTE!!: Use the 'liblinear' solver if using multi-class 1 vs. all classification

## Measurement
Becuase we have a direct classification goal, classification measurements should be used to evaluate the model. These can include:
- Accuracy (how many predictions did the model get right?)
- Precision
- Recall
- F1
