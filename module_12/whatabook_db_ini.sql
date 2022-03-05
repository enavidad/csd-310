
create schema whatabook;
use whatabook;
/*
    Title: db_init.sql
    Author: Edgardo Navidad
    Date: 5 March 2022
    Description: whatabook database initialization.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

-- create location table
CREATE TABLE store(
	store_id	INT 	NOT NULL	AUTO_INCREMENT,
    locale	VARCHAR(500) 	NOT NULL,
    PRIMARY KEY(store_id)
    );
-- create the user table 
CREATE TABLE user(
    user_id     INT             NOT NULL        AUTO_INCREMENT,
    first_name   VARCHAR(75)     NOT NULL,
    last_name      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
); 
-- create book table and set the foreign key
CREATE TABLE book(
	book_id INT	NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200)	NOT NULL,
    author	VARCHAR(200)	NOT NULL,
    details	VARCHAR(500),
    PRIMARY KEY(book_id)
    );
-- create the wishlist table and set the foreign key
CREATE TABLE wishlist(
    wishlist_id   INT	NOT NULL	AUTO_INCREMENT,
    user_id  INT     NOT NULL,
    book_id   INT	NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
		REFERENCES book(book_id),
    CONSTRAINT fk_user 
    FOREIGN KEY(user_id)
        REFERENCES user(user_id)
);


-- insert book info
INSERT INTO book(book_name, author, details)
    VALUES('IT', 'Stephen King', 'Killer clown from space.');
INSERT INTO book(book_name, author, details)
    VALUES('The Fellowship of the Ring', 'J.R. Tolkien','First book of the Lord of the Rings');
INSERT INTO book(book_name, author, details)
    VALUES('The Two Towers', 'J.R. Tolkien', 'The second book of the Lord of the Rings');
INSERT INTO book(book_name, author, details)
    VALUES('The Return of the King', 'J.R. Tolkien', 'The final book of the Lord of the Rings');
INSERT INTO book(book_name, author, details)
    VALUES('Farenheit 451', 'Ray Bradbury', 'Classic book burning');
INSERT INTO book(book_name, author, details)
    VALUES('1984', 'George Orwell', 'Classic dystopian sci-fi novel');
INSERT INTO book(book_name, author, details)
    VALUES('A Song of Fire and Ice', 'George R. R. Martin', 'Dark Fantasy novel');
INSERT INTO book(book_name, author, details)
    VALUES('Enders Game', 'Orson Scott Card', 'Child soldiers fight alien bugs');
INSERT INTO book(book_name, author, details)
    VALUES('Dreamcatcher', 'Stephen King', 'Book about rear aliens');
INSERT INTO book(book_name, author, details)
    VALUES('Dune', 'Frank Herbert', 'Sandworms and trade negotiations');


-- insert store info
INSERT INTO store(locale)
    VALUES('867 Elm Street, Springfield, IL 80085');


-- insert user info
INSERT INTO user(first_name, last_name) 
    VALUES('Thorin', 'Oakenshield');
INSERT INTO user(first_name, last_name) 
    VALUES('Johnny', 'Blaze');
INSERT INTO user(first_name, last_name) 
    VALUES('Bobby', 'Drake');

-- insert wishlist info
INSERT INTO wishlist(user_id, book_id) 
    VALUES(
		(SELECT user_id FROM user WHERE first_name = 'Thorin'),
        (SELECT book_id FROM book WHERE book_name = 'IT')
        );
INSERT INTO wishlist(user_id, book_id) 
    VALUES(
		(SELECT user_id FROM user WHERE first_name = 'Johnny'),
        (SELECT book_id FROM book WHERE book_name = '1984')
        );
INSERT INTO wishlist(user_id, book_id) 
    VALUES(
		(SELECT user_id FROM user WHERE first_name = 'Bobby'),
        (SELECT book_id FROM book WHERE book_name = 'Dune')
        );

use whatabook;
show tables;
