print("#----------------------------------------------------------BConnector----------------------------------------------------------")
import sqlite3
from sqlite3 import OperationalError
from colorama import Cursor
import pymysql.cursors
from secret import impassword
import re


connection = pymysql.connect(
    host='localhost',
    user='root',
    password=impassword,
    db='project0database'
                        )

cursor = connection.cursor()

tq = ""


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

        elif command[0] == "\n":
            command = command[1:]

        if command == "":
            pass

        else:
            try:
                cursor.execute(f"""{command+";"}""")
                print(f"""{command+";"}""")
            except (OperationalError):
                print("Command skipped: ")

executeScriptsFromFile("Testing.sql")

connection.commit()

connection.close()
