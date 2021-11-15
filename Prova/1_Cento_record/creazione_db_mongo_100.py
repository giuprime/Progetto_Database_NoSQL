
from pymongo import MongoClient
import csv


client = MongoClient('localhost', 27017)

nomedb = 'dati100'

miodb = client[nomedb]


dat100 = miodb.dat100


with open(r'C:\Users\giuse\PycharmProjects\Prova\1_Cento_record\dataset100.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        dat100.insert_one({'NAME': row[0], 'CF': row[1], 'EMAIL': row[2], 'CELL': row[3], 'ADDRESS': row[4],
                           'CLAIM': int(row[5]), 'EVALUATED': row[6], 'LAWYER': row[7],
                           'COMPANY': row[8], 'TYPE': row[9], 'STATE': row[10], 'DATE': (row[11])})
        line_count += 1


''' altro tipo d'inserimento 
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)'''