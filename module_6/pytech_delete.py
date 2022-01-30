import pymongo
url = "mongodb+srv://admin:admin@cluster0.mylhl.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client.pytech
col = db.students
col.insert_one({
   "student_id":"1010",
   "first_name":"John",
   "last_name":"Doe",
})

my_query = {"student_id":"1010"}

doc = db.students.find_one({"student_id":"1010"})
col.delete_one(my_query)
doc = db.students.find_one({"student_id":"1010"})
print(doc)