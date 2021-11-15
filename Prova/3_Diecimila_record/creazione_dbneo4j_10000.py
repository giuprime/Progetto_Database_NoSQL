from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
psw = "giuseppe"

driver = GraphDatabase.driver(uri, auth=(user, psw))
session = driver.session()


session.run("CREATE CONSTRAINT ON (a:USER) ASSERT a.cf is unique;")
session.run("CREATE CONSTRAINT ON (b:EVAL) assert b.id_eval is unique;")
session.run("CREATE CONSTRAINT ON (c:CLAIM) assert c.id_cla is unique;")
session.run("CREATE CONSTRAINT ON (d:LAWYER) assert d.id_law is unique;")
session.run("CREATE CONSTRAINT ON (e:COMPANY) assert e.id_company is unique;")



#vengono creati i nodi###
session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv"  AS row
MERGE (a:USER  {cf: row.CF})
ON CREATE SET a.name = row.NAME, a.email= row.EMAIL, a.cell = row.CELL , a.address=row.ADDRESS
ON MATCH SET a.name =row.NAME,  a.email= row.EMAIL, a.cell = row.CELL , a.address=row.ADDRESS 

MERGE (b:EVAL {id_eval : row.EVALUATED})

MERGE (c:CLAIM {id_cla : row.CLAIM})
ON CREATE SET c.type = row.TYPE, c.state = row.STATE, c.date = row.DATE
ON MATCH SET  c.type = row.TYPE, c.state = row.STATE, c.date = row.DATE

MERGE (d:LAWYER {id_law: row.LAWYER})
MERGE (e:COMPANY {id_company: row.COMPANY})

""")


#Vengono create le relazioni #

session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv" AS row
MATCH (a:USER {cf: row.CF}), (c:CLAIM {id_cla: row.CLAIM})
CREATE (a)-[:is_RECALL]->(c)
""")

session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv" AS row
MATCH  (d:LAWYER {id_law: row.LAWYER}), (c:CLAIM {id_cla: row.CLAIM}) 
CREATE (d)-[:is_INVOLVED_LAWYER]->(c)
""")

session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv" AS row
MATCH  (b:EVAL {id_eval: row.EVALUATED}), (c:CLAIM {id_cla: row.CLAIM})
CREATE (b)-[:is_INVOLVED_EVAL]->(c)
""")

session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv" AS row
MATCH  (d:LAWYER {id_law: row.LAWYER}), (e:COMPANY {id_company: row.COMPANY})
CREATE (d)-[:work_FOR_LAWYER]->(e)
""")

session.run("""LOAD CSV WITH HEADERS FROM "file:///dataset10000.csv" AS row
MATCH  (b:EVAL {id_eval: row.EVALUATED}), (e:COMPANY {id_company: row.COMPANY})
CREATE (b)-[:work_FOR_EVAL]->(e)
""")




