import pymongo
url = "mongodb+srv://admin:admin@cluster0.mylhl.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client.pytech
col = db.students

my_query = {"last_name":"Oakenshield"}
new_values = {"$set":{"last_name":"Oakenshield II"}}

col.update_one(my_query,new_values)
doc = db.students.find_one({"student_id":"1007"})
print(doc)