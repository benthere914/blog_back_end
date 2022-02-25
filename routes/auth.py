from validate_email import validate_email
from flask import Blueprint, request
from models import User, db
from flask_login import login_user, current_user, logout_user
auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    # check if user is already logged in
    if (current_user.is_authenticated):
        return {'message': 'you are currently logged in. Please log out to create a new user'}

    # check if user already exists
    new_user_data = request.get_json()
    if (any(User.query.filter(User.email == new_user_data['email']).all())):
        return {'message': 'email exists'}, 401
    if (not validate_email(new_user_data['email'])):
        return {'message': 'email is not valid'}
    # create new user object and check if the user has a valid password
    password = new_user_data['password']
    new_user = User(username=new_user_data['username'], email=new_user_data['email'], password=new_user_data['password'])
    if (not new_user.valid_password(password)[0]):
        return {'message': f' invalid password - {new_user.valid_password(password)[1]}'}, 401
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'success'}


@auth_routes.route('/login', methods=['POST'])
def log_in():
    log_in_data = request.get_json()
    user = User.query.filter(User.email == log_in_data['email']).first()

    if (not any([user])):
        return {'message': 'invalid email'}, 401
    if not user.check_password(log_in_data['password']):
        return {'message': 'invalid password'}, 401

    login_user(user)
    return {'message': 'success'}

@auth_routes.route('/logged_in')
def logged_in():
    return {'logged in': current_user.is_authenticated}



@auth_routes.route('/logout', methods=['POST'])
def log_out():
    if (not current_user.is_authenticated):
        return {'message': 'user is not currently logged in'}, 401
    logout_user()
    return {'message': 'user successfully logged out'}
