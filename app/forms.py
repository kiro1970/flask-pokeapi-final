from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class PokeForm(FlaskForm):
    pokemon1input = StringField('Choose your Pokemon', validators=[DataRequired()])
    pokemon2input = StringField('Opponents Pokemon', validators=[DataRequired()])
    submit = SubmitField()

# class PokeResults(FlaskForm):
#     battlenum = IntegerField('Choose your Pokemon', validators=[DataRequired()])
#     submit = SubmitField()

class LoginForm(FlaskForm):
   name = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')
   
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')