import pymongo
url = "mongodb+srv://admin:admin@cluster0.mylhl.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client.pytech
col = db.students
col.insert_one({
    "student_id":"1007",
  "first_name":"Thorin",
  "last_name":"Oakenshield",
})
col.insert_one({
    "student_id":"1008",
   "first_name":"Bilbo",
   "last_name":"Baggins",
})
col.insert_one({
   "student_id":"1009",
   "first_name":"Frodo",
   "last_name":"Baggins",
})
#doc = db.students.find_one({"student_id":"1007"})
#print(doc)