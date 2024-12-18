from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Authorization(db.Model):
    id_t = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(66), nullable=False)
    surname = db.Column(db.String(66), nullable=False)
    email = db.Column(db.String(66), nullable=False)
    password = db.Column(db.String(66), nullable=False)
    task = db.Column(db.String(666), nullable=True)

    def print_task(self):
        pass
    def __repr__(self):
        return (f'Пользователь: {self.name} {self.surname}'
                f'Прописать функцию print_task!'
                f'Задачи: {self.print_task()}')

