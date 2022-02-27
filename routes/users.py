from flask import Blueprint
from jwt import auth_required, current_user
from models import User
user_routes = Blueprint('users', __name__)

@user_routes.route('/')
def get_users():
    return {"users": [user.to_dict()['username'] for user in User.query.all()]}

@user_routes.route('/me')
@auth_required
def get_user():
    return {'user': current_user().to_dict()}
