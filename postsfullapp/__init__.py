
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cffd88e7a1063b2a76e356cc59551da0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_Manager = LoginManager(app)
login_Manager.login_view = 'login'
login_Manager.login_message_category = 'info'

from postsfullapp import routes