from flask import Flask, render_template
from config import Config
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
print('App is configured')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app) 
login.login_view = 'login'

from . import services
from . import routes
from app import routes, models

