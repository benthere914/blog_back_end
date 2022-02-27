from validate_email import validate_email
from flask import Flask, request
from flask_cors import CORS
from config import Config
from models import db, User
from routes import auth_routes, user_routes
from jwt import guard
# import any blueprints from routes folder
application = Flask(__name__)

application.config.from_object(Config)
application.register_blueprint(auth_routes, url_prefix='/auth')
application.register_blueprint(user_routes, url_prefix='/users')
# register blueprints to application

guard.init_app(application, User)
db.init_app(application)
CORS(application)

if __name__ == "__main__":
    application.debug = True
    application.run()
