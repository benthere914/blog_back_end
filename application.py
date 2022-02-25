from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from config import Config
from models import db, User
from routes import auth_routes, user_routes
# import any blueprints from routes folder

application = Flask(__name__)

login = LoginManager(application)
# login.login_view = 'auth.unauthorized'
@login.user_loader
def load_user(id):
    user = User.query.get(int(id))
    return user

application.config.from_object(Config)
application.register_blueprint(auth_routes, url_prefix='/auth')
application.register_blueprint(user_routes, url_prefix='/users')
# register blueprints to application

db.init_app(application)
CORS(application)
if __name__ == "__main__":
    application.debug = True
    application.run()
