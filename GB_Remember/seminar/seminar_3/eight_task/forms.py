from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.validators import DataRequired, EqualTo

class Valid_Auth(FlaskForm):
    name = StringField('имя', validators=[DataRequired()])
    surname = StringField('фамилия', validators=[DataRequired()])
    email = EmailField('почта', validators=[DataRequired()])
    password = PasswordField('пароль', validators=[DataRequired()])
    confirm_password = PasswordField('подтверждение пароля', validators=[EqualTo('password')])





