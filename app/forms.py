from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    pokemon1input = StringField('Choose your Pokemon', validators=[DataRequired()])
    pokemon2input = StringField('Opponents Pokemon', validators=[DataRequired()])
    submit = SubmitField()

class PokeResults(FlaskForm):
    battlenum = IntegerField('Choose your Pokemon', validators=[DataRequired()])
    submit = SubmitField()

class LoginForm(FlaskForm):
   name = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')
   

