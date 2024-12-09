from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class ValidRegist(FlaskForm):
    first_name = StringField('username', validators=[DataRequired()])
    sure_name = StringField('surname', validators=[DataRequired()])
    login = StringField('login', validators=[DataRequired()])
    password_us = PasswordField('password', validators=[DataRequired()])
    password_confirm = PasswordField('confirm_password', validators=[EqualTo('password_us')])
