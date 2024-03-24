from numpy import mean, std
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

# define dataset
X_data = data.drop('target_var', axis=1)
y_data = data['target_var']

estimator = Pipeline([("scaler", StandardScaler()),
                      ("regression", LinearRegression())])

kf = KFold(shuffle=True, random_state=72018, n_splits=3)  # shuffling the indexis of the rows rather than going in order or in a pattern

#cross_val_predict is a function that does K-fold cross validation for us, appropriately fitting and transforming at every step of the way
predictions = cross_val_predict(estimator, X_data, y_data, cv=kf)  # could also put cv = # of splits. ex: cv = 3 (the data just might not be shuffled)






# define the pipeline
steps = list()
steps.append(('scaler', MinMaxScaler()))
steps.append(('model', LogisticRegression()))
pipeline = Pipeline(steps=steps)

# define the evaluation procedure. Create Cross validation
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=1)

# evaluate the model using cross-validation
scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs=-1)

# report performance
print('Cross-validation accuracy, mean (std): %.2f (%.2f)' % (mean(scores)*100, std(scores)*100))
