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
    print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'],config['host'],config['database']))
    cursor.execute('select team_id, team_name, mascot from team')
    teams = cursor.fetchall()
    print('\n--DISPLAYING TEAM RECORDS--')
    for team in teams:
        print( '\nTeam ID: {}\nTeam Name: {} \nMascot: {}'.format(team[0],team[1],team[2]))
    
    cursor.execute('select player_id, first_name, last_name, team_id from player')
    player = cursor.fetchall()
    print('\n\n --DISPLAYING PLAYER RECORDS')
    for player in player:
        print('\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}'.format(player[0],player[1],player[2],player[3]))
    print('\n\n Press any key to continue...')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('\n The supplied username or password are invalid')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('\n The specified database does not exist')
    else:
        print('\n err')
