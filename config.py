import os
basedir = os.path.abspath(os.path.dirname(__name__))
print('BASEDIR==' + basedir)

class Config:
    FLASK_APP = os.environ.get('FLASK_APP') 
    FLASK_ENV = os.environ.get('FLASK_ENV') 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://kyle:kyle@localhost:5432/RipTide'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

