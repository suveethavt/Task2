import pymongo

connect_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connect_url)

p=client.list_database_names()

mydb=client["Telephone_db"]
collection_db=mydb["Telephone_directory"]

#
#insert one data
document_one={"FirstName":"Thangevel","LastName":"P", "Phone":204806,
           "Place":"samathur",
           "Pin":642231}
collection_db.insert_one(document_one)

ins_one=collection_db.find()



#insert multiple datas
documents_many=[
    {"FirstName":"uma","LastName":"M", "Phone":325886,
           "Place":"poy",
           "Pin":632331},
    {"FirstName":"Muthukumar","LastName":"L", "Phone":204810,
           "Place":"samathur",
           "Pin":642231},
    {"FirstName":"Eswarasamy","LastName":"VP", "Phone":224530,
           "Place":"veeralpet",
           "Pin":632231},
    {"FirstName":"Chandru","LastName":"E", "Phone":222345,
           "Place":"pollachi",
           "Pin":642129},
    {"FirstName":"Suveetha","LastName":"VT", "Phone":232506,
           "Place":"veeralpet",
           "Pin":632231},
    {"FirstName":"Pushpa","LastName":"L", "Phone":342535,
           "Place":"veeralpet",
           "Pin":632231},
    {"FirstName":"Vignesh","LastName":"P", "Phone":257842,
           "Place":"poy",
           "Pin":634682},
    {"FirstName":"Shanthi","LastName":"T", "Phone":318651,
           "Place":"Cbe",
           "Pin":652264},
    {"FirstName":"Panner","LastName":"M", "Phone":324732,
           "Place":"cbe",
           "Pin":652264},
      ]

collection_db.insert_many(documents_many)

ins_many=collection_db.find()
list(ins_many)

#update one data
query={"FirstName":"Suveetha"}
new_one={"$set":{"Place":"poy"}}
collection_db.update_one(query,new_one)

up_date_one=collection_db.find()
list(up_date_one)


#delect one data
query1={"FirstName": "Pushpa"}
collection_db.delete_one(query1)

remove_one=collection_db.find()
list(remove_one)


for i in collection_db.find():
 print(i)

