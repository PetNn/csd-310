# Name: Peter Nnamani
# Class: CYBR410-T301 Data/Database Security (2237-1)
# Date: 08/11/23


-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Rootdb54321';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS wishlist;


-- create the users table 
CREATE TABLE users (
    user_id     INT             NOT NULL        AUTO_INCREMENT,
    first_name   VARCHAR(75)     NOT NULL,
    last_name      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
); 

-- create the books table and set the foreign key
CREATE TABLE books (
    book_id   INT             NOT NULL        AUTO_INCREMENT,
    book_name  VARCHAR(200)     NOT NULL,
    details   VARCHAR(200)     NOT NULL,
    author   VARCHAR(200)     NOT NULL,
    PRIMARY KEY(book_id),
    
);

-- create the store table 
CREATE TABLE store (
    store_id     INT             NOT NULL        AUTO_INCREMENT,
    locale   VARCHAR(500)     NOT NULL,
    PRIMARY KEY(store_id)
); 

-- create the wishlist table and set the foreign key
CREATE TABLE wishlist (
    wishlist_id   INT             NOT NULL        AUTO_INCREMENT,
    user_id     INT             NOT NULL,
    book_id   INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    FOREIGN KEY(user_id)
        REFERENCES users(user_id)
    FOREIGN KEY(book_id)
        REFERENCES books(book_id)
);

-- insert users records
INSERT INTO users(first_name, last_name)
    VALUES('Jane', 'Doe');

INSERT INTO users(first_name, last_name)
    VALUES('John', 'Doe');
INSERT INTO users(first_name, last_name)
    VALUES('Blessing', 'Good');

-- insert books records 
INSERT INTO books(book_name, details, author) 
    VALUES('Hero of Tiger Hill', 'Good book', 'John Doe');

INSERT INTO books(book_name, details, author) 
    VALUES('Bleach', 'Good book', 'James Bankai');

INSERT INTO books(book_name, details, author) 
    VALUES('Overlord', 'Good anime', 'Michael lord');

INSERT INTO books(book_name, details, author) 
    VALUES('For the love of god', 'Not Good', 'Jose Good');

INSERT INTO books(book_name, details, author) 
    VALUES('I hate you', 'Good book', 'Blessing Good');

INSERT INTO books(book_name, details, author) 
    VALUES('life is good', 'Good book', 'Jane Doe');

INSERT INTO books(book_name, details, author) 
    VALUES('One wedding', 'Not good', 'John Doe');

INSERT INTO books(book_name, details, author) 
    VALUES('Love', 'Good book', 'Jane Doe');

INSERT INTO books(book_name, details, author) 
    VALUES('Oh Mother', 'Good book', 'Jose Good');

-- insert store records
INSERT INTO store(locale) 
    VALUES('400 walmart street, Jerseycite,NJ, 07335');

-- insert wishlist records
INSERT INTO books(wishlist_id, user_id, book_id) 
    VALUES('1', '1', '1');
