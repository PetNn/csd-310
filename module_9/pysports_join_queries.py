# Name: Peter Nnamani
# Class: CYBR410-T301 Data/Database Security (2237-1)
# Date: 07/29/23

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
try:
   # connect to the pysports database(db).
    db = mysql.connector.connect(**config) 
    #linking db to the cursor.
    cursor = db.cursor()

    # inner join query to execute and select from.
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    pla = cursor.fetchall()
    # DIsplay and the below statement before executing the for loop.
    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # iterate over the player data set and display the results 
    for player in pla:
        #print the below and format with array with start with [0].
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    # exception if any error occurs
    input("\n  Press any key to continue... ")
     # exception if any error occurs
except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
     # Close the connection

    db.close()