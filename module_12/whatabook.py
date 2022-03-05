from random import choice
import sys
import mysql
import mysql.connector
from mysql.connector import errorcode
config = {
    'user':'whatabook_user',
    'password':'MySQL8IsGreat!',
    'host':'localhost',
    'database':'whatabook',
    'raise_on_warnings':True
}
#Show the menu
def show_menu():
    print('--Main Menu--')
    print('\n1.)Books \n2.)Store Locations \n3.)My Account \n4.)Exit Application')
    try:
        answer = int(input("\nEnter the corresponding number of choice:"))
        return answer
    except ValueError:
        print('\nError. \nInvalid number entered.\n Program Terminating...\n')
        sys.exit(0)

#Option 1:Show Books
def show_books(_cursor):
    _cursor.execute('SELECT book_id, book_name, author, details from book')
    books = _cursor.fetchall()
    print('\n -Displaying Books-')
    for book in books:
        print('\nBook ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}'.format(book[0],book[1],book[2],book[3]))

#Option 2:Show Locations
def show_locations(_cursor):
    _cursor.execute('SELECT store_id, locale FROM store')
    location = _cursor.fetchall()
    print('\n-Displaying Store Locations-')
    for location in location:
        print('\nLocale: {}'.format(location[1]))

#User Validating
def validate_user():
    try:
        user_id = int(input('\nPlease enter a Customer ID:'))
        if user_id < 1 or user_id > 3:
            print('\nInvalid customer ID\nProgram terminating...')
            sys.exit(0)
        return user_id
    except ValueError:
        print('\nInvalid number, program terminating...')
        sys.exit(0)

#Account Menu
def user_menu():
    try:
        print('\n Account Menu')
        print('\n1.)Wishlist\n2.)Add Book\n3.)Main Menu')
        user_choice = int(input('\nPlease enter a number for your choice, 1-3:'))
        return user_choice
    except ValueError:
        print('\nInvalid input, program terminating...')
        sys.exit(0)

#Account Option 1: Display Wishlist
def show_wishlist(_cursor,_user_id):
    _cursor.execute('SELECT user.user_id,user.first_name,user.last_name,book.book_id,book.book_name,book.author' +
        'From wishlist' +
        'INNER JOIN user on wishlist.user_id = user.user_id' +
        'INNER JOIN book on wishlist.book_id = book.book_id' +
        'WHERE user.user_id = {}'.format(_user_id))
    wishlist = _cursor.fetchall()
    print('\n __Displaying Wishlist Items__')
    for book in wishlist:
        print('\nBook Name: {}\nAuthor: {}'.format(book[5],book[6]))

#Show books not on Wishlist
def wishlist_add(_cursor,_user_id):
    query = ('SELECT book_id, book_name, author, details'
    'FROM book'
    'WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})'.format(_user_id))
    print(query)
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print('\n--Displaying Books--')
    for book in books_to_add:
        print('\nBook ID: {}\nBook Name: {}'.format(book[0],book[1]))

#Add book to wishlist
def add_book(_cursor,_user_id, _book_id):
    _cursor.execute('INSERT INTO wishlist(user_id, book_id) VALUES({},{})'.format(_user_id,_book_id))







try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print('\nMySQL Application')
    print('\nWelcome!')

    answer = show_menu()

    while answer !=4:
        if answer == 1:
            show_books(cursor)
        if answer == 2:
            show_locations(cursor)
        if answer == 3:
            my_user_id = validate_user()
            account_option = user_menu()
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor,my_user_id)
                if account_option == 2:
                    show_wishlist(cursor, my_user_id)
                    book_id = int(input('\nEnter the id of the book you want to add:'))
                    add_book(cursor,my_user_id,book_id)
                    db.commit()
                    print('\nBook ID: {} was added to your wishlist.'.format(book_id))
            else:
                print('\nInvalid option.\n Please try again...')
                account_option = user_menu()
    if answer <0 or answer > 4:
        print("\nerror....try again")
        answer = show_menu()
    print('End of Program')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('\n The supplied username or password are invalid')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('\n The specified database does not exist')
    else:
        print('\n err')
finally:
    db.close()