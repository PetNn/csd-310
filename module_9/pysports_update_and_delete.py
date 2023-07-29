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
def show_players(cursor):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    pla = cursor.fetchall()
    #for loop to format and display player
    for player in pla:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()

try: # connection the database
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
   
    # Inserting the value first_name:Smeagol, last_name: Shire Folk, team_id: 1. 
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")
   # commit() to save change to db
    db.commit()

    # printout the below statement before calling the show_players(cursor).
    print("-- DISPLAYING PLAYER AFTER INSERT --")
    show_players(cursor)
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol' ");
    # commit() to save change to db
    db.commit()

    # printout the below statement before calling the show_players(cursor).
    print("-- DISPLAYING PLAYER AFTER UPDATE --")
    show_players(cursor)
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'");
    # commit() to save change to db
    db.commit()

    # printout the below statement before calling the show_players(cursor).
    print("-- DISPLAYING PLAYER AFTER DELETE --")
    show_players(cursor)
    input("Press any key to continue...") # exception if any error occurs.

# exception if any error occurs.
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
finally:
     # Close the connection.
    db.close()
