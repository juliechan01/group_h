import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://amanleyskj:3G2EGv4A4lReDOOY@yiipcluster.of7olmw.mongodb.net/")
db = cluster["yiip"]
user_collection = db["users"]
business_collection = db["businesses"]

connection_string = """
mongodb+srv://amanleyskj:3G2EGv4A4lReDOOY@yiipcluster.of7olmw.mongodb.net/
"""


# posts are like entries in another database; we are inserting 'posts' into the database of users below
# RESEARCH BEING DONE ON MONGODB INTEGRATION; PLEASSSSSE BE PATIENT

post = {"_id" : 0, "name" : "Tim", "score" : 5}

user_collection.insert_one(post)