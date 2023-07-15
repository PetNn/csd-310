#(1)Create a new file under module_6 and name it pytech_delete.py.
#(2)Add the required Python code to connect to the students collection (refer to previous assignments for help).
#(3)Call the find() method and display the results to the terminal window.
#(4)Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
#(5)Call the find_one() method and display the results to the terminal window.
#(6)Call the delete_one() method by student_id 1010.
#(7)Call the find() method and display the results to the terminal window.

                 #(2)
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

                             #(3)
#Call the find() method and display the results to the terminal window.
print(" ")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
stu=stud_conn.find()
for stu_up in stu:
    print(stu_up,'\n')
print(" ")
                              #(4)
# Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
# creating the information to add to the student collection.
MongoDB = {
    "student_id":"1010",
    "first_name":"Jimmy",
    "last_name": "Jake",
    "Role": "student"
    }
# creating stud_insert variable to insert the above document.
stud_insert = stud_conn.insert_one(MongoDB)

                            #(5)
# Call the find_one() method and display the results to the terminal window.
print("-- INSERT STATEMENT --")
print(" ")
print("-- DISPLAYING STUDENT TEST DOC --")
insert_view=stud_conn.find_one({'student_id':'1010'})
print(insert_view)
print(" ")

                      #(6)
#(6)Call the delete_one() method by student_id 1010.
Del_stud= {'student_id': '1010'}
stud_conn.delete_one(Del_stud)

                         #(7)
#Call the find() method and display the results to the terminal window
print("")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
stu=stud_conn.find()
for stu_up in stu:
    print(stu_up,'\n')

# Name: Peter Nnamani.
# Class: CYBR410-T301 Data/Database Security (2237-1).
# Assignment: Module 6.3 Assignment.