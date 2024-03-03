import pandas as pd

filepath="data/iris_data.csv"

data=pd.read_csv(filepath)

"""
DIFFERENT DELIMITERS
sep='\t'               tab-separated file
delim_whitespace=True  space separated file

header=None

SET COLUMN NAMES
pd.read_csv(filepath, names=['col1','col2'])

SET NULL VALUES
pd.read_csv(filepath, na_values=['NA',99])    sets NA or 99 as null values
"""
