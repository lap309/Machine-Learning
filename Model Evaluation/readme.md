* ${R^2}$ - the amount of variability of the data that is able to be explained in the model
* Cost Matrix
* AUC
* Log Loss
* Cumulative Lift

## Classification Metrics
#### Confusion Matrix: 
True Positives, False Positives (Type I Error), True Negatives, False Negatives (Type II Error)
#### Accuracy
not good for imabalanced classes. Out of all the predictions we made, how many were correct? (True Negatives and True Positives)
  $$\frac{TP + TN}{TP + TN + FP + FN} $$
#### Precision:
Out of the observations the model predicted to be positive, how many of those observations are actually positive <br>$$\frac{TP}{TP + FP} $$ Identifying the true positives out of the observations the model predicted to be positive.
#### Recall/Sensitivity/Capture Rate:
From the subpopulation of the positive class (class 1), how many of those people was our model able to identify.   $$\frac{TP }{TP + FN} $$
#### F1 Score:
The harmonic mean of Precision and Recall that tries to capture a balance between this trade off  $$2*\frac{Precision * Recall}{Precision + Recall}$$
  This differs from accuracy because it will more heavily weight if either precision or recall is too low
#### Specificity:
The recall of negative cases. How well can our model predict the true negatives of the subpopulation $$\frac{TN }{FP + TN} $$
#### False Positive: (1- Specificity)
#### ROC Curve: [Better for balanced classes] 
Provides a graphical map of the recall with the flase positive rate on the x axis (1-specificity) and the recall on the y axis. We want to get as close as the top left corner as possible, which would indicate a high recall and a low false positive rate. This can be achieved by changing the probability threshold when determining positive and negative classes
#### ROC AUC: Area under the ROC Curve. 
This measures how well we are separating the two classes.Knowing that we want to be as far off to the left corner as possible, it also means we want as much area under the curve as possible. So the higher the AUC, the better.<br>
An AUC score of .5 means that the model is no better than just guessing
#### Precision-Recall Curve: [Better for UNBALANCED classes] 
plots line charts for these metric scores for different threshold values with recall on the x axis and precision on the y axis. Mostly decreasing lines

#### Multi-Classification Metrics
$Accuracy = \frac{TP Class 1 + TP Class 2 + TP Class 3}{Total n of samples}$<br><br>
There's no directed generalization of ROC, precision-recall and the remainder of the measures, but we can look at both precision-recall, specificity, etc, for each class, as a one versus all approach. We can look at the specificity of class 1 versus the rest, class 2 versus the rest, and so on. 

<br><Br>
from sklearn.metrics import <br>
accuracy_score,<br>
precision_score,<br>
recall_score,<br>
f1_score,<br>
roc_auc_score,<br>
confusion_matrix,<br>
roc_curve,<br>
precision_recall_curve <br><Br>

score = accuracy_score(y_test, y_predictions)
      
