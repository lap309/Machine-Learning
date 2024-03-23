#encoding nominal data
from sklearn.preprocessing import LabelEncoder, LabelBinarizer


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
