import csv
from faker import Faker
import random
from faker_vehicle import VehicleProvider

falso = Faker(('it_IT'))
falso.add_provider(VehicleProvider)
lista_nomi = []
lista_cognomi = []
lista_compagnia = []
lista_avvocati = []
lista_avvocati2 = []
lista_tipologia = ["Danno da incendio", "Furto", "Incidente stradale", "Incidente sul lavoro", "Calamita naturale", "Fenomeno elettrico",
                   "Incidente aereo", "Danno materiale", "Danno fisico", "Danno punitivo", "Danno patrimoniale", "Danno biologico"]
lista_stato = ["Risolto", "Non risolto"]




for w in range (20):
    compagnia_ripetuta = falso.company()
    lista_compagnia.append(compagnia_ripetuta)
for z in range (50):
    nome_ripetuto = falso.first_name()
    cognome_ripetuto = falso.last_name()
    lista_nomi.append(nome_ripetuto)
    lista_cognomi.append(cognome_ripetuto)
    lista_avvocati.append(nome_ripetuto)
    lista_avvocati2.append(cognome_ripetuto)

with open('dataset10000.csv', mode='w', newline='') as csv_file:
    fieldnames = ['NAME', 'CF', 'EMAIL', 'CELL', 'ADDRESS',  'CLAIM', 'EVALUATED', 'LAWYER', 'COMPANY', 'TYPE', 'STATE', 'DATE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    id = 1
    claim = 0
    for x in range(10000):
        name = random.choice(lista_nomi) + " " + random.choice(lista_cognomi)
        cf = falso.ssn()
        email = falso.email()
        cell = falso.phone_number()
        address = falso.address()
        claim += 1
        evaluated = falso.name()
        lawyer = random.choice(lista_avvocati) + " " + random.choice(lista_avvocati2)
        company = random.choice(lista_compagnia)
        type = random.choice(lista_tipologia)
        state = random.choice(lista_stato)
        date = falso.date()
        writer.writerow(
            {
                'NAME': name,
                'CF': cf,
                'EMAIL': email,
                'CELL': cell,
                'ADDRESS': address,
                'CLAIM': claim,
                'EVALUATED': evaluated,
                'LAWYER': lawyer,
                'COMPANY': company,
                'TYPE': type,
                'STATE': state,
                'DATE' : date
            })
id+=1
