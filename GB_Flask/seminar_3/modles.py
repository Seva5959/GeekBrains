from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Это база без которой нельзя.
# конфиг это словарь, ключ менять нельзя, а вот значения меняются в зависимости от СУБД
#                                                                    (система управления база данных)

db = SQLAlchemy() # нужен чисто для взаимодействия с базами данных
# При создании столбиков db.Column можно выбрат 5 типов данных  инт-db.eger стр db.String(228) Булл-db.Boolean флоат-db.Float время-db.DateTime и очень много другого


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Уникальный, а также стоит в начале
    username = db.Column(db.String(80), nullable=False)  # Не может быт пустым
    surename = db.Column(db.String(120), nullable=False)
    sex = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id')) # Делает связь между таблицами на уровне БАЗЫ ДАННЫХ

    def __repr__(self):
        return f'{self.username} {self.surename}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    # Метод relationship делает связь между таблицами на уровне ПАЙТОН ОБЪЕКТОВ
    # backref дает как-бы обратную связь. Теперь объект Student может обратиться по имени 'faculty'
    # lazy=True позволяет lazy=False вызывает ошибку, если обратиться без явного запроса
    posts = db.relationship('Student', backref='faculty', lazy=True)
    # сам posts это список объектов student, в широком смысле слова. Не list
    def __repr__(self):
        return f'{self.name}'
