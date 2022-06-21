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

cursor.execute("""LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedMedicalData.csv" 
INTO TABLE patients 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 ROWS;""")

cursor.execute("""SELECT * FROM patients;""")


def showinfoSQL():
    specificcolumn = "*" #str(input("What column would you want to see? "))
    specifictable = "patients" #str(input("What table would you want to see? "))
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
    insertfirstname = "Jordi"
    insertlastname = "Ictech"
    try:
        cursor.execute(f"""INSERT INTO patients (id,firstname,lastname)
        VALUES({insertid},'{insertfirstname}','{insertlastname}');""")
    except:
        print("Can't add patient in target location.")

def deleteSQL():
    deletelocation = "firstname" #str(input("id, firstname or lastname? "))
    deleteinformation = "Jill" #str(input(f"What is the {deletelocation} for the patient? "))
    try:
        cursor.execute(f"DELETE FROM patients WHERE {deletelocation} = '{deleteinformation}';")

    except:
        print("Patient not found.")


insertSQL()

deleteSQL()

showinfoSQL()



connection.commit()

connection.close()


