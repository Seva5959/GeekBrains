from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id_us = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Integer, nullable=False)
    second_name = db.Column(db.String(60), nullable=False)
    login_us = db.Column(db.String(60), nullable=False)
    password_us = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return (f'Пользователя зовут {self.first_name} {self.second_name}<br> '
                f'Его логин {self.login_us}<br>'
                f'пароль {self.password_us}<br>')