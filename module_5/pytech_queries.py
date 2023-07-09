# Importing the MongoClient file 
from pymongo.mongo_client import MongoClient

# Linking url to connect to the database
uri = "mongodb+srv://admin:admin@cluster0.audxdg6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Creating db variable and linking client to the pytech database
db = client.pytech

# Creating a stud_conn variable to link db variable to students(collection)
stud_conn = db["students"]

# Use the find() method to display all documents in the collection
ddb = stud_conn.find()
for stud_info in ddb: # using for loop to display the all new students
    print(stud_info)

# Use the findOne() method to display a single document by student_id.
print(stud_conn.find_one({"student_id": "1007"}))