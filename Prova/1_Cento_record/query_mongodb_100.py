from pymongo import MongoClient
import time
import xlsxwriter

client = MongoClient('localhost', 27017)

nomedb = 'dati100'

miodb = client[nomedb]


dat100 = miodb.dat100

def tempo(): return int(round(time.time() * 1000))


def query_uno(name):
    lista = []
    for x in dat100.aggregate([{"$count": name}]):
        lista.append(x)
    return lista

def query_due(name, cf):
    lista = []
    for x in dat100.find( {"NAME": name}, {"CF": cf} ).sort("NAME", 1):
        lista.append(x)
    return lista
def query_tre(name, cf, email):
    lista = []
    for x in dat100.find({"NAME": name , "CF": cf, "EMAIL": email}):
        lista.append(x)
    return lista

def query_quattro (name, cf, email, cell):
    lista = []
    for x in dat100.find({"NAME": name , "CF": cf, "EMAIL": email, "CELL": cell}):
        lista.append(x)

    return lista
def query_cinque (name, cf, email, cell, address):
    lista = []
    for x in dat100.find({"NAME": name , "CF": cf, "EMAIL": email, "CELL": cell, "ADDRESS":{"$regex": address}}).sort("CF", 1):
        lista.append(x)

    return lista

workbook = xlsxwriter.Workbook('Risultati100mongo.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0

for y in range(31):
    a1 = tempo()

    #"Lucia Bernardini"
    #query_uno("Lucia Bernardini")
    #query_due("Lucia Bernardini","XZPPXD81W61N187A")
    #query_tre("Lucia Bernardini","XZPPXD81W61N187A", "fusaniennio@gmail.com")
    #query_quattro("Lucia Bernardini","XZPPXD81W61N187A", "fusaniennio@gmail.com", "+39 15 73177355")
    query_cinque("Lucia Bernardini","XZPPXD81W61N187A", "fusaniennio@gmail.com", "+39 15 73177355", "Via")

    a2 = tempo()
    worksheet.write(row, col, a2 - a1)
    row += 1

    print("abbiamo ottenuto il (", y + 1, "°) risultato in", a2 - a1, "millisecondi\n")


worksheet.write(row, col, a2-a1)
workbook.close()