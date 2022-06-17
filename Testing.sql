DROP TABLE IF EXISTS Testing;

CREATE TABLE Testing (
ID int NOT NULL,
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Age int,
PRIMARY KEY (ID)
);

INSERT INTO Testing (ID,PersonID,LastName,FirstName,Age)
VALUES (1,143,"west",'Gerogios',31), (2,267,"Ola","Hansen",30),(3,395,'Svendson','Tove',23);