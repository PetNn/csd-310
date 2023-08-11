#Name: Peter Nnamani
# Class: CYBR410-T301 Data/Database Security (2237-1)
# Date: 08/11/23

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "Rootdb54321",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
 
#creating a show_menu function to show the menu for WhatABook.
def show_menu():
     # print to display the menu for users      
    print("Welcome to Whatabook menu options!")
    print("Press '1 to view Books.")
    print("Press '2 to view Store Locations.")
    print("Press '3 to view My Account.")
    print("Press '4 to view Exit Whatabook menu options.")

#creating a show_book function to show the books for WhatABook.
def show_books(cursor):
    #. Display book records and fetchall for the books table
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING BOOK RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[1]))
        print("Author Name: {}".format(book[3]))
        print()
#creating a show_location function to show the store for WhatABook.    
def show_locations(cursor):
   #. Display book records and fetchall for the books table
    cursor.execute("SELECT * FROM store")
    locations = cursor.fetchall()
    print("-- DISPLAYING LOCATION RECORDS --")
    for location in locations:       
        print("Locale: {}".format(location[1]))
#. Creating a function to validate user
def validate_user(cursor, user_id):
    if len (user_id) == 0:
        return False
    try:
        cursor.execute(f"SELECT * FROM user WHERE user_id=\"{int(user_id)}\"")
        userlist = cursor.fetchall()
        return len(userlist) == 1
    except ValueError:
        return False
# Creating function to valid book_id
def validate_book(cursor,book_id):
    if len (book_id) == 0:
        return False
    try:
        cursor.execute(f"SELECT * FROM book WHERE book_id=\"{int(book_id)}\"")
        booklist = cursor.fetchall()
        return len(booklist) == 1
    except ValueError:
        return False
# creating a function that let grant user access to the personal account information
def run_my_account():
    user_id=input("Enter your user_id:")
    if validate_user(cursor, user_id):
        user_choice = 5
        while user_choice !="3":
            show_account_menu()            
            user_choice=input("Enter your choice:")
            if user_choice == "1":
                show_wishlist(cursor, user_id)                       
            if user_choice == "2":
                        show_books_to_add(cursor, user_id)
                        book_id=input("Enter the Book ID:")
                        if validate_book(cursor, book_id):
                            add_book_to_wishlist(cursor, user_id, book_id)
                        else: 
                           print("invalid Book ID:")
                           print()                        
            if user_choice not in ("1","2","3"):
                        print("Enter '1,'2,'3")
            if user_choice == "3":
                        print("Going back to Main Menu.")
    else:
        print("invalid User ID.")
# creating a function that display Account menu.
def show_account_menu():
    print("Here is the Account Menu:")
    print("Enter 1 for Wishlist")
    print("Enter 2 to add a Book")
    print("Enter 3 to return to Main Menu")

# creating a function that display wishlist
def show_wishlist(cursor, user_id):
    # using INNER JOIN to create and join wishlist book_id, book(book-id) and user_id.
    cursor.execute("SELECT * FROM wishlist INNER JOIN book on wishlist.book_id = book.book_id WHERE user_id = " + user_id.strip())
    wishlist = cursor.fetchall()
    for row in wishlist:
        print("")
        print(row[4])

# creating a function that will display books for user to add
def show_books_to_add(cursor, user_id):
    cursor.execute("SELECT book_name, author, book_id FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING WISHLIST RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[0]))
        print("Author Name: {}".format(book[1]))
        print("Book ID: {}".format(book[2]))
# creating a function that let user add book to wishlist
def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute(f"INSERT INTO wishlist (user_id,book_id) VALUES ({user_id},{book_id})")
    #This is to finalize changes to the database.
    db.commit()
try:
    #Standard initialization to the database.
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()

    user_choice=5
    while user_choice !="4":
        show_menu()       
        user_choice=input("Please enter your choice:")
        if user_choice == "1":
            show_books(cursor)
        if user_choice == "2":
            show_locations(cursor)
        if user_choice == "3":
            run_my_account()
        if user_choice == "4":
            print("Goodbye")
        if user_choice not in ("1","2","3","4"):
            print("Please enter '1,'2,'3,'4")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exist")

    else:
        print(err)
finally:
    db.close()