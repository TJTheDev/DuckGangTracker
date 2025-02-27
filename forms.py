from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, NumberRange

import app


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    #password = StringField('password', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    #password = StringField('password', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    team = SelectField('team', coerce=int)

class IncreaseForm(FlaskForm):
    increment = IntegerField('Number of Pushups', validators=[DataRequired(), NumberRange()])

class TeamForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
