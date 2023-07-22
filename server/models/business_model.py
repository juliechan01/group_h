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

    @classmethod
    def save(cls, data_row):
        query = """
        INSERT INTO businesses(type, name, address, phone_number, business_hours, offerings) 
        VALUES (%(type)s, %(name)s, %(address)s, %(phone_number)s, %(business_hours)s, %(offerings)s)
        """

        # creating other class methods soon