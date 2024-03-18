from . import db

class Properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    num_bedrooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    type = db.Column(db.String(50))
    description = db.Column(db.Text)
    photo_filename = db.Column(db.String(100))



    def __init__(self, title, num_bedrooms, num_bathrooms, location, price, type, description, photo_filename):
        self.title = title
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo_filename = photo_filename



        def get_id(self):
            return str(self.id)    