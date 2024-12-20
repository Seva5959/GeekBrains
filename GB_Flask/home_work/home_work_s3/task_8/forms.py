from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.validators import DataRequired, EqualTo

class Valid_Auth(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[EqualTo('password')])

