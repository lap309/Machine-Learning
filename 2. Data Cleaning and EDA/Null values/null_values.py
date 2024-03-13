
def find_nulls(df):
    null_count = df.isnull().sum().sort_values(ascending = False)
    null_percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
    nulls_df=pd.concat([null_count, null_percent], axis=1, keys=['Count', 'Percent'])
    nulls_df= nulls_df[nulls_df["Percent"] > 0]
    f,ax =plt.subplots(figsize=(8,6))
    plt.xticks(rotation='90')
    fig=sns.barplot(nulls_df.index, nulls_df["Percent"],color="green",alpha=0.8)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Percent of missing values', fontsize=15)
    plt.title('Percent missing data by feature', fontsize=15)
    return nulls_df

######## IMPUTING WITH LINEAR REGRESSION
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
