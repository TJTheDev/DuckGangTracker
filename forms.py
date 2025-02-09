from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class IncreaseForm(FlaskForm):
    increment = IntegerField('Number of Pushups', validators=[DataRequired(), NumberRange()])
