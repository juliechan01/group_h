from flask import Flask
import os
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)

# accessing the password from another file
password = os.getenv("m-pwd")

load_dotenv()
# enabling CORS to work (allows 3000 and 8080 communication)
cors = CORS(app)
print(f"This is the password: {password}")
connection_string = f"mongodb+srv://amanleyskj:{password}@yiipcluster.of7olmw.mongodb.net/"
print(f"This is the connection string: {connection_string}")

# mongoclient is a method at which I"m passing in a connection point
client = MongoClient(connection_string)

# paul soda-opolis will know more about this, so reach out to him (Brendan suggestion)
app.config["MONGO_URI_TRACK_MODIFICATIONS"] = False
app.config["MONGO_URI"] = f"mongodb+srv://amanleyskj:{password}@yiipcluster.of7olmw.mongodb.net/"
