# Name: Peter Nnamani
# Class: CYBR410-T301 Data/Database Security (2237-1)
# Date: 07/22/23

# importing a connection to MySql
import mysql.connector
from mysql.connector import errorcode

# creating a link to the Sql Server with config
config = {
    "user": "pysports_user",
    "password": "Rootdb54321",  # Password 
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
# Creating a try and exception to catch errors.
try:# connect to the pysports database.
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}". format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

# exception if any error occurs 
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
        
finally:
    # Close the connection
    db.closed()
    
