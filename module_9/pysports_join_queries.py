import mysql
import mysql.connector
from mysql.connector import errorcode
config = {
    'user':'root',
    'password':'root',
    'host':'localhost',
    'database':'pysports',
    'raise_on_warnings':True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute('select player_id, first_name, last_name, team_name\
        from player\
        inner join team\
             on player.team_id = team.team_id')

    result = cursor.fetchall()
    print('\n\n --DISPLAYING PLAYER RECORDS--')
    for x in result:
         print('\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}'.format(x[0],x[1],x[2],x[3]))
    print('\n\n Press any key to continue...')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('\n The supplied username or password are invalid')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('\n The specified database does not exist')
    else:
        print('\n err')
