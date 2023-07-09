# Importing the MongoClient file 
from pymongo.mongo_client import MongoClient

# Linking url to connect to the database
uri = "mongodb+srv://admin:admin@cluster0.audxdg6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # print this below statement if successfully connected 
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Creating db variable and linking client to the pytech database
db = client.pytech
# printing the collection(tables) in pytech using the .list_collection_names()
print(db.list_collection_names())

# The Students collection wouldn't show until information is inserted.