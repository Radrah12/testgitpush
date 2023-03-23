import pymongo
client = pymongo.MongoClient("mongodb+srv://raghavrahul1991:8VWzL6e0hYyUCIZS@cluster0.8ajbf5s.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudhanshu@gmailcom",
    "surnmae" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)