from pymongo import *


# pravljenje konekcije koriscenjem MongoClient-a

client = MongoClient('localhost', 27017)
db = client.drus

# ocitavanje kolekcije student  iz MongoDB Compass-a

collectionstudent = db.student
cursor = collectionstudent.find({})

for document in cursor:
    print(document)

# ubacivanje dokumenta u kolekciju student.
# Cilj: pojvaljivanje novog dokumenta u kolekciji student.

collectionstudent = db["student"]
document1 = {"ime": "Pera",
        "prezime": "Peric",
        "brojIndeksa": "EM20/2014"}

document_id = collectionstudent.insert_one(document1)

collectionstudent = db["student"]
document2 = {"ime": "Tijana",
        "prezime": "Pavlovic",
        "brojIndeksa": "EM5/2014"}

document_id = collectionstudent.insert_one(document2)

collectionstudent = db["student"]
document3 = {"ime": "Natasa",
        "prezime": "Panic",
        "brojIndeksa": "EM13/2014"}

document_id = collectionstudent.insert_one(document3)

collectionstudent = db["student"]
document4 = {"ime" : "Marko",
             "prezime": "Markovic",
             "brojIndeksa" : "EM15/2014"}

document_id = collectionstudent.insert_one(document4)

# ocitavanje kolekcije predmet iz MongoDB Compass-a

collectionpredmet = db.predmet
cursor1 = collectionpredmet.find({})

for documents in cursor1:
    print(documents)

# ubacivanje dokumenta u kolekciju predmet.
# Cilj: pojvaljivanje novog dokumenta u kolekciji student.

collectionpredmet = db["predmet"]
documents1 = {"Naziv": "Inteligentni upravljacki sistemi",
        "Profesor": "V.Bugarski",
        "ESPB": "6"}

documents_id = collectionpredmet.insert_one(documents1)

collectionpredmet = db["predmet"]
documents2 = {"Naziv": "Distribuirani upravljacki sistemi",
        "Profesor": "A. Erdeljan",
        "ESPB": "6"}

documents_id = collectionpredmet.insert_one(documents2)

collectionpredmet = db["predmet"]
documents2 = {"Naziv": "Adaptivno i napredno upravljanje",
        "Profesor": "M. Rapaic",
        "ESPB": "6"}

documents_id = collectionpredmet.insert_one(documents2)

collectionpredmet = db["predmet"]
documents2 = {"Naziv": "Totalno integirsani SAU",
        "Profesor": "V.Congradac",
        "ESPB": "6"}

documents_id = collectionpredmet.insert_one(documents2)
