# Make it so python sends to csv and then executes the MYSQL script. The MYSQL script reads the CSV and updates the table. Python can also ask for specific IDs from a premade database in MYSQL.

print("#----------------------------------------------------------Connector----------------------------------------------------------")
print("#----------------------------------------------------------Test----------------------------------------------------------")
from sqlite3 import OperationalError
import pymysql.cursors
from secret import impassword

connection = pymysql.connect(
    host='localhost',
    user='root',
    password=impassword,
    db='project0database'
                        )

cursor = connection.cursor()

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands

        if command == "":
            pass

        else:
            try:
                cursor.execute(command)
                print("Executed")
            except (OperationalError):
                print("Command skipped: ")

executeScriptsFromFile("ImportingCSV.sql") #Add filename here

connection.commit()

connection.close()
