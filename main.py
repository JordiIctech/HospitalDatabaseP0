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














