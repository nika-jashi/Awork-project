from db import db


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(56), unique=True, nullable=False)
    first_name = db.Column(db.String(56), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
