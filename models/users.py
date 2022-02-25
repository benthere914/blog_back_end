from .db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)


    def valid_password(self, password):
        if (not (any([char for char in password if char in '01234567890']))):
            return [False, 'a number']
        if (not (any([char for char in password if char in '`~!@#$%^&*()_-+={[}]|\\;:\'",<.>/?']))):
            return [False, 'any special characters']
        if (not any([char for char in password if char in [letter.upper() for letter in 'abcdefghijklmnoppqrstuvwxyz']])):
            return [False, 'any upper case letters']
        if (len(password) < 8):
            return [False, 'at least 8 characters']
        return [True, '']
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
