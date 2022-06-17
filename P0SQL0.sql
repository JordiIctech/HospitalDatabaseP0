/* create database 
CREATE DATABASE project0database;
*/
USE project0database;

SET GLOBAL local_infile=1; # allows for csv file imports.

SET SQL_SAFE_UPDATES = 0;

SHOW TABLES;

SELECT * FROM Testing;

/*

DROP TABLE IF EXISTS Persons;
CREATE TABLE Persons (
ID int NOT NULL,
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Age int,
PRIMARY KEY (ID)
);

SHOW TABLES;
INSERT INTO Persons (ID,LastName,FirstName,Age)
VALUES (1,"west",'Geroge',31), (2, "Ola","Hansen",30),(3,'Svendson','Tove',23);

SELECT * FROM Persons;


SHOW DATABASES;

#Normalize data

*/

