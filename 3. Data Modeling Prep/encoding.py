#encoding nominal data
from sklearn.preprocessing import LabelEncoder, LabelBinarizer


# Determine how many extra columns would be created
category_columns = data.columns[data.dtypes == object]
num_ohc_cols = (data[categorical_columns]
                .apply(lambda x: x.nunique())
                .sort_values(ascending=False))

small_num_ohc_cols = num_ohc_cols.loc[num_ohc_cols>1]     # No need to encode if there is only one value
small_num_ohc_cols -= 1                # Number of one-hot columns is one less than the number of categories
small_num_ohc_cols.sum()           #prints the number of columns that would be created if one hot encoded


#one hot encoder will remove the base column while get_dummies will not

from sklearn.preprocessing import OneHotEncoder


from pandas import get_dummies


dummies = pd.get_dummies(data['col'], drop_first = True)           #create the dummies
data = pd.concat([data, dummies], axis = 1)                      # add the dummies to the original df
data.drop(['col'], axis = 1, inplace = True)                         # drop the original column

# encoding ordinal/ordered variables
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder

### Label Encoding with .replace()
df['col'].replace({'old_val1': 'new_val1', 
           'old_val2' : 'new_val2',
           'old_val3': 'new_val3'}, 
           inplace= True)
