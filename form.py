from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class Signup(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=12)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField('confirm password', validators=[DataRequired(), Length(min=8), EqualTo('password')])

    submit = SubmitField('sign up ')


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=12)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    stay_login = BooleanField('Stay_login')
   
    submit = SubmitField('login')

class Home(FlaskForm):
    bedrooms = StringField('Number of bedrooms', validators=[DataRequired()])
    bathrooms = StringField('Number of bathrooms')

    submit = SubmitField('Search')