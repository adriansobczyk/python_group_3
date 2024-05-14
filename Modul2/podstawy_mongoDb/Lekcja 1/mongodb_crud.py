'''
Operacje CRUD na bazie danych MongoDB
'''

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# CREATE

client = MongoClient(
    "mongodb://localhost:27017/",
    server_api=ServerApi('1')
)

# Option 1
db = client["book"]

# Option 2
# db = client.book

print(db)

# result_one = db.cats.insert_one(
#     {
#         "name": "Mruczek",
#         "age": 3,
#         "features": ["załatwia się w buty", "pozwala się głaskać", "rudy"],
#     }
# )

# print(result_one.inserted_id)

# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["chodzi do kuwety", "nie pozwala się głaskać", "szary"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["chodzi do kuwety", "pozwala się głaskać", "biały"],
#         },
#     ]
# )
# print(result_many.inserted_ids)


# READ

# result = db.cats.find_one({"_id": ObjectId("6643aaa9c03423dbf755e0e3")}) # OBJECT ID będzie inny dla każdego dokumentu
# print(result)


# UPDATE
# db.cats.update_one({"name": "Mruczek"}, {"$set": {"age": 4}})
# result = db.cats.find_one({"name": "Mruczek"})
# print(result)


# DELETE

# db.cats.delete_one({"name": "Mruczek"})
# result = db.cats.find_one({"name": "Mruczek"})
# print(result)