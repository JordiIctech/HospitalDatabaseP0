import names
import random as rnd
import csv

print("#----------------------------------------------------------Data Generator----------------------------------------------------------")

MaleFirstNames = []
FemaleFirstNames = []
LastNames = []
symptoms = ["Cough","Sneezing","Fatigue", "Inflamation", "Headache"]


for i in range(5):                                                      # Makes 5 male first names.
    MaleFirstNames.append(names.get_first_name(gender='male'))

for i in range(5):                                                      # Makes 5 female first names.
    FemaleFirstNames.append(names.get_first_name(gender='female'))

for i in range(10):
    LastNames.append(names.get_last_name())

#for i in range(5):
#    print(MaleFirstNames[i] + " " + LastNames[i])

#for i in range(5):
#    print(FemaleFirstNames[i] + " " + LastNames[i+5])

personID = rnd.randint(0,4)

print(MaleFirstNames[personID] + " " + LastNames[personID] + ":")

print(rnd.choices(symptoms,weights=(1,1,1,1,1),k=(rnd.randint(1,4)))) #list, weights=odds per item, *, cum_weights=odds per item out of 100, # of items picked

rows = []
 
# field names
fields = ["ID",'First Name', 'Last Name'] # Add ID
htnames = int(len(LastNames)/2) # Half of Total Number of nNames
print(htnames)

for i in range(0,int(htnames)):
    rows.append([i+1,MaleFirstNames[i],LastNames[i]]) # Add a third entry just with number i being passed

for i in range(0,int(htnames)):
    rows.append([i+htnames+1,FemaleFirstNames[i],LastNames[i+htnames]]) # Add a third entry just with number i being passed

print(rows)

filename = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneratedMedicalData.csv"

with open(filename, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
     
    csvwriter.writerows(rows)

