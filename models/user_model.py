from flask_app.config import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    db = "users"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.first_name = data_row['first_name']
        self.last_name = data_row['last_name']
        self.email = data_row['e    mail']
        self.password = data_row['password']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']
        self.my_pictures = []

        @classmethod
        def save(cls, data_row):
            query = """
            INSERT INTO users(first_name, last_name, email, password) 
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
            """

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
            return is_valid
