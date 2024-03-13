import sqlite3 as sq3
import pandas as pd

# Download the database
!wget -P data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/classic_rock.db
path="data/classic_rock.db"    #make sure this is the folder where the database lives

#create connection to SQL database
con=sq3.Connection(path)

#Write query
query="""

"""

#Execute query
data=pd.read_sql(query, con)

########################################################################################################
#Jupity Notebooks

import sqlite3 as sq3            # will connect to the SQLLite3 database. you might be using a different database
# SQLAlchemy [Microsoft SQL Server]
# psycopg2 [Postgres]
# MySQLdb [MySQL]
# AWS Redshift
# AWS Aurora
#Oracle DB
# Terradata
# Db2 Family

import pandas.io.sql as pds
import pandas as pd
!wget -P data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/classic_rock.db
path="data/classic_rock.db"
con = sql3.Connect(path)    #implements a live connection to the SQL database

query="""
"""

#Execute the query
output = pds.read_sql(query, con)
output.head()


"""Notes:Common parameters/functions
couerce_float: attempts to force numbers into floats
parse_dates: list of columns to parse as dates
chunksize: number of rows to include in each chunk"""

observations = pds.read_sql(query, con,
                              coerce_float = True,
                              parse_dates=['Release_Year'],
                              chunksize=5)


