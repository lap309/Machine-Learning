#JSON files are very similar to Python dictionaries in structure

import pandas as pd
filepath=" "

#read JSON file as dataframe
data=pd.read_json(filepath)

#write dataframe file to JSON
data.to_json(outputfile_name.json)
