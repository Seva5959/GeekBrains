from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id_us = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return (f'Пользователя зовут {self.name} {self.surname}<br> '
                f'Его логин {self.email}<br>'
                f'пароль {self.password}<br><br>')