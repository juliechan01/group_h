from flask_app import app
from flask import flash
import re
from pymongo import MongoClient
from flask_pymongo import PyMongo
import pprint
from bson.objectid import ObjectId

from flask_app.controllers import user_controller, home_controller, business_controller

db = PyMongo(app)

printer = pprint.PrettyPrinter()
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.email = data_row['email']
        self.password = data_row['password']
        self.birthday = data_row['birthday']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.my_pictures = []

        # must create save() class method for new users
        # must create edit() class method for users to edit their profile
        @classmethod
        def register_user(data_row):
            # this is a test; for a real function, we'll be tying in data from the frontend
            # insert_one is a built-in function of collection saccess
            user_collection.insert_one(data_row)
            # gives us the ID of what was just inserted into the collection
            inserted_id = user_collection.insert_one(data_row)._id
            print(f"The id of {inserted_id} has been created and should now reflect in the database.")

        @classmethod
        def get_user_by_id(user_id):
            # below import can be put somewhere else; this just makes it self-contained
            from bson.objectid import ObjectId

            # we need to convert to the following because they need to be this special object; the strings we have as IDs aren't going to work here
            _id = ObjectId(user_id)

            user = user_collection.find_one({"_id" : _id})
            printer.pprint(user)

        @classmethod
        def get_by_email(email):
            user_email = user_collection.find_one({"email" : email})
            
        @classmethod
        def find_all_users():
            users = user_collection.find()

            for user in users:
                printer.pprint(user)

        @classmethod
        def update_user_by_id(user_id):
            from bson.objectid import ObjectId
            _id = ObjectId(user_id)

            all_updates = {
                #set operater sets a new field to be a value of our choice; it can also be used to change a value to existing field
                "$set" : {"new_field" : True},
                "$set" : {"age" : 5},
                #increment is $inc; this will increment the age of what we're modifying by 1; the $inc works fine, but it must be an incrementable data type
                # "$inc" : {"birthday" : "111"},
                # rename is for updating the name of a field
                "$rename" : {"Mihogirl" : "first_name", "Manley" : "last_name"}
            }
            # updating all things in the user field
            user_collection.update_one({"_id" :  _id}, all_updates)
            # below is for unsetting a field (in other words, removing something from the document)
            user_collection.update_one({ "_id" : _id}, { "$unset" : {"new_field" : ""}})

        @classmethod
        def delete_user_by_id(user_id):
            from bson.objectid import ObjectId
            _id = ObjectId(user_id)
            user_collection.delete_one({"_id" : _id})
            # for deleting many documents; currently it would delete EVERYTHING


        @staticmethod
        def validate_user(form):
            is_valid = True
            if len(form['first_name']) < 2:
                is_valid = False
                flash("Your first name must be two characters or more.")
            if len(form['last_name']) < 2:
                is_valid = False
                flash("Your last name must be two characters or more.")
            if not EMAIL_REGEX.match(form['email']):
                is_valid = False
                flash("Your email address must be in a valid format.")
            if len(form['password']) < 8:
                is_valid = False
                flash("Your password must be eight characters or more.")
            if not form['password'] == form['confirm_password']:
                is_valid = False
                flash("Your passwords must match.")
            if (form['birthday']) < 18:
                is_valid = False
                flash("You must be 18 years old or older to join yiip.")
            return is_valid