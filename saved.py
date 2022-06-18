
print("#----------------------------------------------------------Connector----------------------------------------------------------")
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

        else:
            try:
                cursor.execute(command)
                print("Executed")
            except (OperationalError):
                print("Command skipped: ")

executeScriptsFromFile("Testing.sql")

connection.commit()

connection.close()


print("#----------------------------------------------------------Main----------------------------------------------------------")
import pymysql.cursors

from secret import impassword

connection = pymysql.connect(
    host='localhost',
    user='root',
    password=impassword,
    db='project0database'
                        )

cursor = connection.cursor()

sql = "SELECT * FROM persons"
cursor.execute(sql)

# Fetch all the records and use a for loop to print them one line at a time
result = cursor.fetchall()
for i in result:
    print(i)

cursor.execute("""DROP TABLE IF EXISTS Testing;""")
cursor.execute("""
CREATE TABLE Testing (
ID int NOT NULL,
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Age int,
PRIMARY KEY (ID)
);""")
cursor.execute("""
INSERT INTO Testing(ID,PersonID,LastName,FirstName,Age)
VALUES (1,143,"west",'Gerogy',31), (2,267,"Ola","Hansen",30),(3,395,'Svendson','Tove',23);"""
)

connection.commit()

connection.close()


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




#--------------------------------------------------------------------------------------








