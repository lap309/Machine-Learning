from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression( penalty='12', c=10)
        #penalty refers to the regularization parameter (l1 -> lasso, l2 -> ridge)
        # c refers to the inverse of the lambda coefficient in the regularization penalty. higher c means less penalty (opposite of lambda)
logreg = LogisticRegression().fit(X_train, y_train)

logreg.score(X_train,y_train)

#see coefficients
logreg.coef_

#make predictions
y_pred = logreg(x_train)



#### Logistic Regression with Cross Validation
from sklearn.linear_model import LogisticRegressionCV
lr_l1 = LogisticRegressionCV(Cs=10, cv=4, penalty='l1', solver='liblinear').fit(X_train, y_train)


# Predicting the probabilities rather than just the class
logreg.predict_proba(x_train)

########## Multi-Class Logistic Regression (rewatch videos for the code)
