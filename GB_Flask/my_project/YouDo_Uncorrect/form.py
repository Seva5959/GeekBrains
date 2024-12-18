from wtforms import StringField, PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo

class ValidForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_confirm = PasswordField('Подтвердите пароль', validators=[EqualTo('password')])
    task = StringField('Задачи', validators=[DataRequired()])
