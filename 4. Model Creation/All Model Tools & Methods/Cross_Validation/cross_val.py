from numpy import mean, std
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

# define dataset
X_data = data.drop('target_var', axis=1)
y_data = data['target_var']

#################### instantiating k-fold
#regular k-fold
kf = KFold(shuffle=True, random_state=72018, n_splits=3)  # shuffling the indexis of the rows rather than going in order or in a pattern

#stratified k_fold
strat_kf = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=1)

##################### instantiate Cross Validation
#cross_val_predict is a function that does K-fold cross validation for us, appropriately fitting and transforming at every step of the way

# EVALUATE the k-fold models with cross_calidation
# define the pipeline
steps = list()                                          # create a pipeline with all the methods you want to apply
steps.append(('scaler', MinMaxScaler()))
steps.append(('model', LogisticRegression()))
pipeline = Pipeline(steps=steps)

#utilize cross validation to test the pipeline methods and find the combination with the best score
scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=kf,        # could also put cv = # of splits. ex: cv = 3 (the data just might not be shuffled)
                         n_jobs=-1)
# print performance
print('Cross-validation accuracy, mean (std): %.2f (%.2f)' % (mean(scores)*100, std(scores)*100))


#Make predictions with the method combination with the best score from above
best_estimator = Pipeline([("scaler", StandardScaler()),
                      ("regression", LinearRegression())])
predictions = cross_val_predict(best_estimator, X_data, y_data, cv=kf)  



