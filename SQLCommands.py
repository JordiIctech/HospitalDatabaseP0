print("#----------------------------------------------------------Main----------------------------------------------------------")
#Need MYSQL Open

import pymysql.cursors

from secret import impassword

connection = pymysql.connect(
    host='localhost',
    user='root',
    password=impassword,
    db='project0database'
                        )

cursor = connection.cursor()

cursor.execute("""DROP TABLE IF EXISTS patients;""")

cursor.execute("""CREATE TABLE patients (
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);""")

cursor.execute("""LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedPAtientData.csv" 
INTO TABLE patients 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 ROWS;""")

cursor.execute("""SELECT * FROM patients;""")


def showinfoSQL():
    specificcolumn = str(input("What column would you want to see? "))
    specifictable = str(input("What table would you want to see? (patients, symptoms, disease)"))
    try: 
        sql = f"SELECT {specificcolumn} FROM {specifictable}"
        cursor.execute(sql)

        result = cursor.fetchall()
        for i in result:
            print(i)
    except:
        print("Table or Row not found.")


def insertSQL():
    insertid = 11
    insertfullname= input("What is the patient's full name? ")
    fullnamelist = insertfullname.split(" ")
    insertfirstname = fullnamelist[0]
    insertlastname = fullnamelist[1]
    try:
        cursor.execute(f"""INSERT INTO patients (id,firstname,lastname)
        VALUES({insertid},'{insertfirstname}','{insertlastname}');""")

    except:
        print("Can't add patient in target location.")

def deleteSQL():
    deletelocation = str(input("id, firstname or lastname? "))
    deleteinformation = str(input(f"What is the {deletelocation} for the patient? "))
    try:
        cursor.execute(f"DELETE FROM patients WHERE {deletelocation} = '{deleteinformation}';")
        
        cursor.execute(f"DELETE FROM symptoms WHERE patientn = '{deleteinformation}';")
    except:
        print("Patient not found.")

def saveSQL():
    connection.commit()

#insertSQL()

#deleteSQL()

#showinfoSQL()


connection.commit()

#connection.close()


