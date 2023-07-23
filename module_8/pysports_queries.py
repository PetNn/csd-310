# Name: Peter Nnamani
# Class: CYBR410-T301 Data/Database Security (2237-1)
# Date: 07/22/23

# importing a connection to MySql
import mysql.connector
from mysql.connector import errorcode

# creating a link to the Sql Server with config
config = {
    "user": "pysports_user",
    "password": "Rootdb54321", # Password 
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
 
 # Creating a try and exception to catch errors.
try:
    # connect to the pysports database.

    db = mysql.connector.connect(**config)  

    cursor = db.cursor()

    # select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # iterate over the players and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
     # ask for input to continue.
    input("\n\n  Press any key to continue... ")

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