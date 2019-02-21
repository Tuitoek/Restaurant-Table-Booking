from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap=Bootstrap()
db = SQLAlchemy()
<<<<<<< HEAD
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'
=======
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
>>>>>>> cc10d6db2d1bec2d52b5c9ac1f44cefcb2115b53

def create_app(config_name):
    app= Flask(__name__)

<<<<<<< HEAD
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # login.init_app(app)


    # login.init_app(app

=======
>>>>>>> cc10d6db2d1bec2d52b5c9ac1f44cefcb2115b53
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # login.init_app(app)

    return app
