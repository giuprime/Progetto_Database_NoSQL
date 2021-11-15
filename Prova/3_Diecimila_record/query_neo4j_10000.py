from neo4j import GraphDatabase
import time
import xlsxwriter

uri = "bolt://localhost:7687"
user = "neo4j"
psw = "giuseppe"

driver = GraphDatabase.driver(uri, auth=(user, psw))
session = driver.session()



def tempo(): return int(round(time.time() * 1000))

def query_1(name):
    query_1 = """MATCH (a:USER) WHERE a.name = $name  
                 RETURN count(a.name) AS conta"""
    risultati = session.run(query_1, name = name)
    dati = [dato["conta"] for dato in risultati]
    return dati

def query_2(name, cf):
    query_2 =      """MATCH (a:USER)-[r:is_RECALL]->(c:CLAIM) 
                      WHERE  a.name = $name OR 
                             a.cf = $cf 

                      RETURN r AS tipo_relazione, c AS richiamo, a AS utente
                      ORDER BY a.name"""
    risultati = session.run(query_2, name = name, cf = cf)
    dati = [dato["utente"] for dato in risultati]

    return dati

def query_3(name, cf, email):
    query_3= """        MATCH   (a:USER)-[r1:is_RECALL]->(c:CLAIM),
                                (b:EVAL)-[r2:is_INVOLVED_EVAL]->(c:CLAIM)<-[r3:is_INVOLVED_LAWYER]-(d:LAWYER)
                        WHERE   a.name = $name AND
                                a.cf = $cf AND
                                a.email = $email 
                        RETURN a AS utente, r1, c AS richiamo, r2, r3
                        """

    risultati = session.run(query_3, name = name, cf = cf, email = email)
    dati = [dato["utente"] for dato in risultati]

    return dati

def query_4(name, cf, email, cell):
    query_4 = """MATCH  (a:USER)-[r1:is_RECALL]->(c:CLAIM),
                        (b:EVAL)-[r4:is_INVOLVED_EVAL]->(c:CLAIM)<-[r5:is_INVOLVED_LAWYER]-(d:LAWYER),
                        (b:EVAL)-[r6:work_FOR_EVAL]->(e:COMPANY)<-[r7:work_FOR_LAWYER]-(d:LAWYER)    
                 WHERE  a.name = $name AND
                        a.cf = $cf AND
                        a.email = $email AND 
                        a.cell = $cell 
                        
                        
       
                 RETURN a AS utente,  b as perito, c AS richiamo, d as avvocato, r1
                 
                 """


    risultati = session.run(query_4, name = name, cf = cf, email = email,cell = cell )
    dati = [dato["utente"] for dato in risultati]

    return dati

def query_5(name, cf, email, cell, address):
    query_5 = """MATCH  (a:USER)-[r1:is_RECALL]->(c:CLAIM),
                        (b:EVAL)-[r4:is_INVOLVED_EVAL]->(c:CLAIM)<-[r5:is_INVOLVED_LAWYER]-(d:LAWYER),
                        (b:EVAL)-[r6:work_FOR_EVAL]->(e:COMPANY)<-[r7:work_FOR_LAWYER]-(d:LAWYER)
                        
                 WHERE  a.name = $name AND
                        a.cf = $cf AND
                        a.email = $email AND
                        a.cell = $cell AND
                        a.address STARTS WITH $address 
                        

                 RETURN a AS utente, b AS Perito, c AS richiamo, d AS avvocato, e AS Compagnia, r1, r4, r5, r6, r7
                 ORDER BY a.cf
              """

    risultati = session.run(query_5, name= name, cf = cf, email = email, cell = cell, address = address)
    dati = [dato["utente"] for dato in risultati]
    return dati

workbook = xlsxwriter.Workbook('RisultatiDati10000Neo4j.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0

for y in range(31):
    a1 = tempo()
    #query_1("Calogero Monaco")
    #query_2("Calogero Monaco","FXCANK25H58K325Y")
    #query_3("Calogero Monaco","FXCANK25H58K325Y", "zbello@ferraris.it")
    #query_4("Calogero Monaco","FXCANK25H58K325Y", "zbello@ferraris.it", "+39 5421 02360680")
    query_5("Calogero Monaco","FXCANK25H58K325Y", "zbello@ferraris.it", "+39 5421 02360680", "Canale")
    a2 = tempo()
    print("abbiamo ottenuto il (", y + 1, "°) risultato in", a2 - a1, "millisecondi\n")

    worksheet.write(row, col, a2 - a1)
    row += 1

worksheet.write(row, col, a2 - a1)
workbook.close()
session.close()
driver.close()