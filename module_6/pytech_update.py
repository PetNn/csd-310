# Create a new directory under csd-310 and name it module_6.
# Inside the module_6 directory create a new file and name it pytech_update.py.
# Add the required Python code to connect to the students collection (refer to previous assignments for help).
# (1)Call the find() method and output the documents to the terminal window.
# (2)Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name.
# (3)Call the find_one method by student_id 1007 and output the document to the terminal window.


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

# (1)Call the find() method and output the documents to the terminal window.
print(" ")
print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")
stu=stud_conn.find()
for stu_up in stu:
    print(stu_up,'\n')

# (2)Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name.
edi_update= {'student_id': '1007'}
ed_update= { "$set": {'last_name': 'Smith' } }
stud_conn.update_one(edi_update,ed_update)

# (3)Call the find_one method by student_id 1007 and output the document to the terminal window.
print(" ")
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
insert_view=stud_conn.find_one({'student_id':'1007'})
print(insert_view)


# Name: Peter Nnamani.
# Class: CYBR410-T301 Data/Database Security (2237-1).
# Assignment: Module 6.2 Assignment.