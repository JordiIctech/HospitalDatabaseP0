USE project0database;

SELECT 
    id, firstname, lastname
FROM
    patients
INTO OUTFILE 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\SQLReturnExport.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';