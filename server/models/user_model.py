from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    db = "users"

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