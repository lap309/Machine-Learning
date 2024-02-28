#Most NoSQL databases are going to store data in the JSON format

from pymongo import MongoClient    #can use other NoSQL databases instead of Mongo
con=MongoClient()                #also implement a username or password here if that's necessary

#with this connectino, we can choose a specific database  
#will display available database
con.list.database_names()

#select specific database
db=con.database_name

#make the query. make sure it's a MongoDB query or a query that matches the type of database you're using
query="""
"""

#create a cursor object using a query. this will just hold all the JSON files
cursos=db.collection_name.find(query)

#expand cursor and construct our JSON files-->list of python dictionaries --> dataframe
df=pd.DataFrame(list(curosr))
