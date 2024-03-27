Using the Sigmoid Function, all values or inputs of x will be between 0 and 1,and will represent the probability of the sample being in a certain class. The class that x-value is assigned to depends on the determined probability threshold.<br><Br>

Odds RAtio

## Multi-class Logistic Regression
Utilizes the technique, 1 vs. all: <br>
ex: class 1, class 2, class 3 <br> <br>

We run a logistic regression of ]:<br>
Class 1 vs. Everything Else (Class 2 and Class 3) to define the decision boundary for Class 1<br>
Class 2 vs. Everything Else (Class 1 and Class 3) to define the decision boundary for Class 2<br>
Class 3 vs. Everything Else (Class 1 and Class 2) to define the decision boundary for Class 3<br><Br>
At the end, we end up with 3 logistic models splitting out their own probability. So the probability that x is in class 1, the probability that x is in class 2, and the probability that x is in class 3. And we take the model with the highest probability and assign x to that category.
