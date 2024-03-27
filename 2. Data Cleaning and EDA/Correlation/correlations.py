#Identify correlations
df_num= df.select_dtypes(include = ['float64', 'int64'])
df_corr = df_num.corr()['target_var'][:-1] # -1 means that the latest row is SalePrice
top_features = df_corr[abs(df_corr) > 0.5].sort_values(ascending=False) #displays pearsons correlation coefficient greater than 0.5
print("There is {} strongly correlated values with target variable:\n{}".format(len(top_features), top_features))

# Build pair plots to visually inspect the correlation between the features and the target variable
for i in range(0, len(df_num.columns), 5):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i:i+5],
                y_vars=['target_var'])

#Create the correlation matrix
corr_values = df_num.corr()
