/* manage database */
USE project0database;

SET GLOBAL local_infile=1; # allows for csv file imports.

SET SQL_SAFE_UPDATES = 0;

DROP TABLE IF EXISTS Persons;
CREATE TABLE Persons (
ID int NOT NULL,
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Age int,
PRIMARY KEY (ID)
);
INSERT INTO Persons (ID,PersonID,LastName,FirstName,Age)
VALUES (1,143,"west",'Geroge',31), (2,267,"Ola","Hansen",30),(3,395,'Svendson','Tove',23);

SELECT * FROM Persons;

SHOW TABLES;

#Normalize data

/*
*/


