##### !!!!! If you don't drop one column from each set of new dummy variables, it will lead to compelte multicollinearity becasue the values of one column would be dependent on the values of another column

# Determine how many extra columns would be created
category_columns = data.select_dtypes(include = ['object', 'category']).columns.tolist()
category_df = data[[category_columns]]

num_ohc_cols = (data[category_columns]
                .apply(lambda x: x.nunique())
                .sort_values(ascending=False))

small_num_ohc_cols = num_ohc_cols.loc[num_ohc_cols>1]     # No need to encode if there is only one value
small_num_ohc_cols -= 1                # Number of one-hot columns is one less than the number of categories
small_num_ohc_cols.sum()           #prints the number of columns that would be created if one hot encoded

################# encoding CATEGORICAL DATA
#pandas get_dummies
from pandas import get_dummies
dummies = pd.get_dummies(data['col'], drop_first = True)           #create the dummies
data = pd.concat([data, dummies], axis = 1)                      # add the dummies to the original df
data.drop(['col'], axis = 1, inplace = True)                         # drop the original column

# sklearn OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
#will return a sparse matrix, which is very helpful with large datasets and saving space, but bad for interpretability/readability
#Good for NLP where you would have a lot of columns from tokenizing
ohe = OneHotEncoder(drop='First')
ohe_data = ohe.fit(data).transform(data)

pd.DataFrame(ohe_data.toarray())    #turning the sparse matrix into a df (for readability). will look like a normal df

# in definition form
def encode(cat_data):
  encoder = OneHotEncoder()
  cat_cols = data.select_dtypes(include = ['object', 'category']).columns.tolist()
  for col in cat_cols:
    # one hot encode the data -- this returns a sparse array  
      dummy_cols = encoder.fit_transform(cat_data[[col]])  
      #dummy_cols = ohc.fit_transform(dat.reshape(-1,1)) #alternative way with reshaping
    
      # Remove the original column from the dataframe
      cat_data.drop(col, axis=1, inplace = True)       

    # Get names of all unique values in column (this will be used to autoamte renaming the columns)  
      cats=encoder.categories_
    # Create unique column names for each dummy variable created in the encoder
      new_col_names = ['_'.join([col,cat]) for cat in cats[0]]

    # Create the new dataframe
      new_df = pd.DataFrame(dummy_cols.toarray(), 
                          #index=cat_data.index, 
                          columns=new_col_names)

    # Append the new data to the dataframe
      encoded_df = pd.concat([cat, new_df], axis=1)
  return encoded_df

################# encoding NOMINAL DATA
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
#one hot encoder will remove the base column while get_dummies will not
le= LabelEncoder()
data['label_col'] = le.fit_transform(data['label_col'])


################# encoding ORDINAL/ORDERED VALUES
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder

### Label Encoding with .replace()
df['col'].replace({'old_val1': 'new_val1', 
           'old_val2' : 'new_val2',
           'old_val3': 'new_val3'}, 
           inplace= True)
