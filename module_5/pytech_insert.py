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
# Insert three new student documents. using arrays
MongoDB = [{
    "student_id":"1007",
    "first_name":"Fred",
    "last_name": "lee",
    "Role": "student"
    },
    {
    "student_id":"1008",
    "first_name":"Peter",
    "last_name": "Haas",
    "Role": "student"

    },{
    "student_id":"1009",
    "first_name":"John",
    "last_name": "Jane",
    "Role": "student"
    }
]
# inserting above new student into pytech using (.insert_many) since we are installing more than one doc. 
fred_student_id = stud_conn.insert_many(MongoDB).inserted_id
# Printing out the list of inserted new student.
print(fred_student_id)