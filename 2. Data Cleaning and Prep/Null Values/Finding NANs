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
