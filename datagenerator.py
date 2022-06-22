import names
import random as rnd
import csv
from pymysql import NULL

print("#----------------------------------------------------------Data Generator----------------------------------------------------------")
    
MaleFirstNames = []
FemaleFirstNames = []
LastNames = []
symptomslists = []

def patientnamegenerate():
    for i in range(5):                                                      # Makes 5 male first names.
        MaleFirstNames.append(names.get_first_name(gender='male'))

    for i in range(5):                                                      # Makes 5 female first names.
        FemaleFirstNames.append(names.get_first_name(gender='female'))

    for i in range(10):
        LastNames.append(names.get_last_name())

    personID = rnd.randint(0,4)

    rows = []
    
    # field names
    fields = ["ID",'First Name', 'Last Name'] # Add ID
    htnames = int(len(LastNames)/2) # Half of Total Number of nNames
    #print(htnames)

    for i in range(0,int(htnames)):
        rows.append([i+1,MaleFirstNames[i],LastNames[i]]) # Add a third entry just with number i being passed

    for i in range(0,int(htnames)):
        rows.append([i+htnames+1,FemaleFirstNames[i],LastNames[i+htnames]]) # Add a third entry just with number i being passed

    #print(rows)

    filename = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedPatientData.csv"

    with open(filename, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)
        
        csvwriter.writerows(rows)

symptoms = ["Cough","Sneezing","Fatigue", "Inflamation", "Headache"]

#Make patients, symptoms(link both patients to disease and mortality rates), disease (analyze ti get average mortality),

##print(rnd.choices(symptoms,weights=(1,1,1,1,1),k=(rnd.randint(1,4)))) #list, weights=odds per item, *, cum_weights=odds per item out of 100, # of items picked

def symptomcreator():  
    #modifiedsymptomkey = len(symptomkey)+100 #Counts characters in string to make key, + 100 for uniqueness.
    for i in range(0,len(LastNames)):
        print("----------------Generating---------------")
        ranquant = rnd.randint(1,5)                          # Makes random number of symptoms
        symptomselection = rnd.sample(symptoms, ranquant)    # Choses random symptoms based on number of symptoms
        symptomselection.sort()                              # Puts them in order
        symptomkey = [",".join(symptomselection)] #Joins strings into on
        symptomselectionV2 = [NULL,NULL,NULL,NULL,NULL] #symptomselectionV2 = ["NULL", "NULL", "NULL", "NULL", "NULL"]
        for z in range(0,len(symptomselection)):
            symptomselectionV2[z]=symptomselection[z]

        symptomselectionV2.insert(0,i+1)
        symptomslists.append(symptomselectionV2)
        print(symptomselectionV2)
    
    filename = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedSymptomData.csv"
    with open(filename, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["PatientN", "Symptoms"])
        
        csvwriter.writerows(symptomslists)

#patientnamegenerate()

#symptomcreator()
