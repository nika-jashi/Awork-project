from db import db


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(56), nullable=False)
    city = db.Column(db.String(56), nullable=False)
    street_address = db.Column(db.String(128), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)




