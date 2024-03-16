#encoding nominal data
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder
from pandas import get_dummies

#one hot encoder will remove the base column while get_dummies will not

# encoding ordinal/ordered variables
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder

### Label Encoding with .replace()
df['col'].replace({'old_val1': 'new_val1', 
           'old_val2' : 'new_val2',
           'old_val3': 'new_val3'}, 
           inplace= True)
