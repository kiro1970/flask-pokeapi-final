from flask import Flask, render_template
from config import Config
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
print('App is configured')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import services
from . import routes
from app import routes, models
