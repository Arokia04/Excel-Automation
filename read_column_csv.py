import csv  

with open('sample.csv') as myFile:  
    reader = csv.DictReader(myFile)
    for row in reader:
        print(row['Value'])
