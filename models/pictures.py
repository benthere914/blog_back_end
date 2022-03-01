from .db import db

class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=False, unique=True)
