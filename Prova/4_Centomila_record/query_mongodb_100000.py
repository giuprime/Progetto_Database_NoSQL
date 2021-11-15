from pymongo import MongoClient
import time
import xlsxwriter

client = MongoClient('localhost', 27017)

nomedb = 'dati100000'

miodb = client[nomedb]


dat100000 = miodb.dat100000

def tempo(): return int(round(time.time() * 1000))


def query_uno(name):
    lista = []
    for x in dat100000.aggregate([{"$count": name}]):
        lista.append(x)
    return lista

def query_due(name, cf):
    lista = []
    for x in dat100000.find( {"NAME": name}, {"CF": cf} ):
        lista.append(x)
    return lista
def query_tre(name, cf, email):
    lista = []
    for x in dat100000.find({"NAME": name , "CF": cf, "EMAIL": email}):
        lista.append(x)
    return lista

def query_quattro (name, cf, email, cell):
    lista = []
    for x in dat100000.find({"NAME": name , "CF": cf, "EMAIL": email, "CELL": cell}):
        lista.append(x)

    return lista
def query_cinque (name, cf, email, cell, address):
    lista = []
    for x in dat100000.find({"NAME": name , "CF": cf, "EMAIL": email, "CELL": cell, "ADDRESS":{"$regex": address}}).sort("CF", 1):
        lista.append(x)

    return lista

workbook = xlsxwriter.Workbook('Risultati100000mongo.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0

for y in range(31):
    a1 = tempo()


    #query_uno("Mattia Moccia")
    #query_due("Mattia Moccia","ONPWVP58G73L022N")
    #query_tre("Mattia Moccia","ONPWVP58G73L022N", "lpennetta@cainero.eu")
    #query_quattro("Mattia Moccia","ONPWVP58G73L022N", "lpennetta@cainero.eu", "+39 01 3912349")
    query_cinque("Mattia Moccia","ONPWVP58G73L022N", "lpennetta@cainero.eu", "+39 01 3912349", "Rotonda")

    a2 = tempo()
    worksheet.write(row, col, a2 - a1)
    row += 1

    print("abbiamo ottenuto il (", y + 1, "°) risultato in", a2 - a1, "millisecondi\n")


worksheet.write(row, col, a2-a1)
workbook.close()