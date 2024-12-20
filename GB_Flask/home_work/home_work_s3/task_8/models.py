from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id_us = db.Column(db.Integer, primary_key=True)
    name_us = db.Column(db.String(60), nullable=False) # попробовать String(10)
    surname_us = db.Column(db.String(60), nullable=False)
    email_us = db.Column(db.String(60), nullable=False)
    password_us = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return (f'Пользователя зовут {self.name_us} {self.surname_us}<br> '
                f'Его логин {self.email_us}<br>'
                f'пароль {self.password_us}<br><br>')


