use project0database;

DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
    patientid INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    PRIMARY KEY (patientid)
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedPatientData.csv" 
INTO TABLE patients 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM patients;

DROP TABLE IF EXISTS symptoms;
CREATE TABLE symptoms (
    patientn VARCHAR(255) NOT NULL,
    s1 VARCHAR(255) NOT NULL,
    s2 VARCHAR(255),
    s3 VARCHAR(255),
    s4 VARCHAR(255),
    s5 VARCHAR(255),
    PRIMARY KEY (patientn)
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedSymptomData.csv" 
INTO TABLE symptoms 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM symptoms;

DROP TABLE IF EXISTS disease;
CREATE TABLE disease (
    diseaseid VARCHAR(255) NOT NULL,
    diseasen VARCHAR(255) NOT NULL,
    s1 VARCHAR(255) NOT NULL,
    s2 VARCHAR(255),
    s3 VARCHAR(255),
    PRIMARY KEY (diseaseid)
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedDiseaseData.csv" 
INTO TABLE disease 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM disease