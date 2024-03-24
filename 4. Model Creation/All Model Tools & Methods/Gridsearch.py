from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Normalizer

#create the pipeline
n_splits=2
kf = KFold(n_splits = n_splits)

estimator = Pipeline([
  ('polynomial_features', PolynomialFeatures()),
  ('scaler', [StandardScaler(), MinMax()]),
  ('regularization',[Ridge(), Lasso()])
   ])

#These parameter values will be iterated in the pipeline to be run and evaluated in the gridsearch
#note: the name of the parameter for each method in the pipeline has to match the name in the pipeline, then add 2 underscores '_' (not just 1)
params= {
  'polynomail_features__degree': [1,2,3],
  'regularization__alpha': np.geomspace(4,20,30)
}


grid = GridSearchCV(estimator, params, cv = kf)    #instantiate Gridsearch
grid.fit( X, y)                                    # fit Gridsearch

grid.best_score_, grid.best_params                  # evaluate the best model

#predict values
y_pred = grid.predict(X)


#puts the combinations and scores of each iteration of the gridsearch into a dataframe
pd.DataFrame(grid.cv_results_))
