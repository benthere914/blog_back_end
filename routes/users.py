from validate_email import validate_email
from flask import Blueprint, request
from flask_login import current_user, login_required
from models import User, db
user_routes = Blueprint('users', __name__)

@user_routes.route('/')
def get_users():
    return {"users": [user.to_dict()['username'] for user in User.query.all()]}

@user_routes.route('/me')
@login_required
def get_user():
    return current_user.to_dict()
