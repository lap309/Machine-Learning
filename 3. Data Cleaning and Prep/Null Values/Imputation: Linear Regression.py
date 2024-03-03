### Takes the data frame, x, and y, and will calculate the mean 


nulls = df['MINIMUM_PAYMENTS'].isnull()
not_nulls = ~nulls

target = df['MINIMUM_PAYMENTS'][not_nulls]
others = list(col for col in df.columns if col not in ['MINIMUM_PAYMENTS','CUST_ID'])
features = df[others][not_nulls]


from sklearn.linear_model import LinearRegression

def impute_lin_reg(df, x, y):
  '''need find_na function (Machine-Learning/Null Values/find_na)
  Input:
  df = dataframe
  x = independent variables
  y = dependent variable

  '''
  
  
  lin_reg = LinearRegression()
  lin_reg.fit(x, y)
  lin_reg.predict(nulls)
  lin_reg.score(features[not_nulls], target)
