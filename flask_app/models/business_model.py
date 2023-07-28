from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user_model

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Business:

    db = "mydb"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.biz = data_row['biz']
        self.name = data_row['name']
        self.address = data_row['address']
        self.phone = data_row['phone']
        self.hours = data_row['hours']
        self.service = data_row['service']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']

##### CREATE
##### CREATE
##### CREATE
    @classmethod
    def save( cls, data_row ):
        query = """
        INSERT INTO businesses (biz, name, address, phone, hours, service)
        VALUES (%(biz)s, %(name)s, %(address)s, %(phone)s, %(hours)s, %(service)s);
        """

        business_name = data_row['name']
        results = connectToMySQL(cls.db).query_db( query, data_row)
        
        print(f"The business {business_name} has been made.")
        return results


### READ
### READ
### READ
    @classmethod
    def get_all_businesses(cls):
        all_businesses = []
        query = "SELECT * FROM businesses"
        results = connectToMySQL(cls.db).query_db(query)
        return all_businesses.append(results)

    @classmethod
    def get_all_businesses_with_user(cls):
        query = "SELECT * FROM businesses JOIN users ON businesses.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_businesses = []
        for data_row in results:
            single_business = cls(data_row)
            single_business_user_info = {
                'id' : data_row['users.id'],
                'biz' : data_row['biz'],
                'name' : data_row['name'],
                'address' : data_row['address'],
                'phone' : data_row['phone'],
                'first_name' : data_row['first_name'],
                'last_name' : data_row['last_name'],
                'email' : data_row['email'],
                'password' : data_row['password'],
                'created_at' : data_row['users.created_at'],
                'updated_at' : data_row['users.updated_at']
            }

            business_creator = user_model.User(single_business_user_info)
            # single_business.creator = business_creator
            all_businesses.append(single_business)
        return all_businesses

    
    @classmethod
    def get_business_with_user(cls,data):
        query = """
        SELECT * FROM businesses LEFT JOIN users ON businesses.user_id = users.id WHERE businesses.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        business = cls(results[0])

        user_data = {
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'birthday' : results[0]['birthday'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        business.creator = user_model.User(user_data)
        print("Business is as follows: ", business)
        return business
    
    @classmethod
    def get_one_business(cls,data):
        query = "SELECT * FROM businesses WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    # @classmethod
    # def get_random_business(cls):
        
    #     num = random.random()
    #     query = "SELECT * FROM businesses LEFT JOIN users ON businesses.user_id = users.id WHERE businesses.id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     return cls(results[0])



### UPDATE
### UPDATE
### UPDATE
    @classmethod
    def edit_business(cls,data):
        query = """
                UPDATE businesses SET id = %(id)s, biz = %(biz)s, name = %(name)s, 
                address = %(address)s, phone = %(phone)s, 
                hours = %(hours)s, service = %(service)s WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results


### DELETE
### DELETE
### DELETE
    @classmethod
    def delete_business(cls, data_row):
        query = """
                DELETE FROM businesses WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data_row)
        return results



    @staticmethod
    def validate_business(form):
        is_valid = True
        if form['biz'] == '':
            is_valid = False
            flash("Please provide a type.")
        if form['name'] == "":
            is_valid = False
            flash("Give us a business name.")
        if form['address'] == '':
            is_valid = False
            flash("Please include an address.")
        if form['phone'] == '':
            is_valid = False
            flash("You must include a phone number.")
        if form['hours'] == '':
            is_valid = False
            flash("Please provide business hours.")
        if form['service'] == '':
            is_valid = False
            flash("What does this business do?")
        return is_valid