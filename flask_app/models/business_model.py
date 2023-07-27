from flask import flash

class Business:

    db = "businesses"

    def __init__( self, data_row ):
        self.id = data_row['id']
        self.type = data_row['type']
        self.name = data_row['name']
        self.address = data_row['address']
        self.phone_number = data_row['phone_number']
        self.business_hours = data_row['business_hours']
        self.offerings = data_row['offerings']
        self.created_at = data_row['created_at']
        self.updated_at = data_row['updated_at']

        # must create getAll() class method me for index page
        # must create getOneBusiness() class method
        # must create editBusiness() class method to allow user to edit his/her business