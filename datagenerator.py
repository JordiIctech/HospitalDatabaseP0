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
    symptomkeys=[]
    for i in range(0,len(LastNames)):
        print("----------------Generating---------------")
        ranquant = rnd.randint(1,5)                          # Makes random number of symptoms
        symptomselection = rnd.sample(symptoms, ranquant)    # Choses random symptoms based on number of symptoms
        symptomselection.sort()                              # Puts them in order
        symptomkey = [",".join(symptomselection)] #Joins strings into on
        symptomkeys.append(symptomkey)
        symptomselectionV2 = [NULL,NULL,NULL,NULL,NULL] #symptomselectionV2 = ["NULL", "NULL", "NULL", "NULL", "NULL"]
        for z in range(0,len(symptomselection)):
            symptomselectionV2[z]=symptomselection[z]
            #print(symptomkeys)

        symptomselectionV2.insert(0,i+1)
        symptomslists.append(symptomselectionV2)
        print(symptomkey)
        print(symptomkeys[i])
#Order: Rhinitis, Flu, Common Cold, Migraine
        if "Inflamation" in symptomkey:
            if "Sneeze" in symptomkey:
                if "Fatigue" in symptomkey:
                    print("--------Rhinitis----------")

        elif "Sneeze" in symptomkey:
            if "Fatigue" in symptomkey:
                if "Cough" in symptomkey:
                    print("----------Flu-------")

        elif "Sneeze" and "Fatigue" and "Runny Nose" in symptomkeys[i]:
            print("----------Common Cold-------")

        elif "Fatigue" and "Headache" in symptomkeys[i]:
            print("----------Migraine-------")

        elif "Sneeze" in symptomkeys[i]:
            print("----------Allergy-------")    

        elif "Runny Nose" in symptomkeys[i]:
            print("----------Common Cold-------")

        elif "Cough" in symptomkeys[i]:
            print("----------Respiratory Infection-------")
        
        elif "Inflamation" in symptomkeys[i]:
            print("----------Area Dependant-------")

        elif "Fatigue" in symptomkeys[i]:
            print("----------Lack of Sleep-------")
        
    
    filename = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedSymptomData.csv"
    with open(filename, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["PatientN", "S1","S2","S3","S4","S5"]) # Need to add disease ID
        
        csvwriter.writerows(symptomslists)

    

#patientnamegenerate()

# DISEASES ------------------------------------------------------------

def diseasecreator():  
    print("----------------Generating---------------")
    
    listeddiseases = ["Flu","Common Cold", "Migraine", "Rhinitis", "Allergy", "Area Dependant", "Common Cold", "Lack of Sleep", "Respiratory Infection"]
    symptomsperdisease=[[101,"Flu","Sneeze", "Fatigue", "Cough"],[102,"Common Cold", "Sneeze", "Fatigue", "Runny Nose"],[103,"Migraine", "Fatigue", "Headache",NULL],[104,"Rhinitis", "Inflamation", "Sneezing", "Fatigue"],[105,"Allergy", "Sneeze",NULL,NULL],[106,"Area Dependant", "Inflamation",NULL,NULL],[107,"Common Cold","Runny Nose",NULL,NULL],[108,"Lack of Sleep", "Fatigue",NULL,NULL],[109,"Respiratory Infection", "Coughing",NULL,NULL]]

    filename = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedDiseaseData.csv"
    with open(filename, 'w', newline='') as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["DiseaseID","Disease","S1","S2","S3"]) # Headlines
            
        csvwriter.writerows(symptomsperdisease) # Rows [[]] list of lists, each inner list is a row.

    # Flu: Sneeze, Fatigue, Cough
    # Common Cold: Sneeze, Fatigue, Runny Nose
    # Migraine: Fatigue, Headache
    # Rhinitis: Inflamation, Sneezing, Fatigue
    # Allergy: Sneeze
    # Area Dependant: Inflamation
    # Common Cold: Runny Nose
    # Lack of Sleep: Fatigue
    # Respiratory Infection: Coughing
   
    
#diseasecreator()
#patientnamegenerate()
#symptomcreator()

# Future work: Create symptom table, show mortality rates.
# Make a list of possible disease rather than just one.