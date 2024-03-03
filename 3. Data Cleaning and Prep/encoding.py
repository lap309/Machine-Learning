#encoding nominal data
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder
from pandas import get_dummies

#one hot encoder will remove the base column while get_dummies will not

# encoding ordinal/ordered variables
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OrdinalEncoder
