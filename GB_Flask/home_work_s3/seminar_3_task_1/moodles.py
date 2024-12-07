from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

sc_direction = {'Him Bio': 1, 'Soc Economy': 2, 'Fitz Math': 3}
students_data = {
    # Направление "Him Bio"
    'Him Bio': [
        {'username': 'Alexei', 'surename': 'Ivanov', 'sex': 'man'},
        {'username': 'Irina', 'surename': 'Petrova', 'sex': 'woman'},
        {'username': 'Mikhail', 'surename': 'Sidorov', 'sex': 'man'},
        {'username': 'Elena', 'surename': 'Kuznetsova', 'sex': 'woman'},
        {'username': 'Dmitry', 'surename': 'Fedorov', 'sex': 'man'},
        {'username': 'Natalia', 'surename': 'Morozova', 'sex': 'woman'},
        {'username': 'Pavel', 'surename': 'Semenov', 'sex': 'man'}
    ],

    # Направление "Soc Economy"
    'Soc Economy': [
        {'username': 'Vladimir', 'surename': 'Smirnov', 'sex': 'man'},
        {'username': 'Maria', 'surename': 'Alexandrova', 'sex': 'woman'},
        {'username': 'Oleg', 'surename': 'Novikov', 'sex': 'man'},
        {'username': 'Svetlana', 'surename': 'Vasilieva', 'sex': 'woman'},
        {'username': 'Andrei', 'surename': 'Karpov', 'sex': 'man'},
        {'username': 'Tatiana', 'surename': 'Orlova', 'sex': 'woman'},
        {'username': 'Roman', 'surename': 'Kozlov', 'sex': 'man'}
    ],

    # Направление "Fitz Math"
    'Fitz Math': [
        {'username': 'Ivan', 'surename': 'Gavrilov', 'sex': 'man'},
        {'username': 'Anna', 'surename': 'Nikolaeva', 'sex': 'woman'},
        {'username': 'Konstantin', 'surename': 'Belyaev', 'sex': 'man'},
        {'username': 'Olga', 'surename': 'Klimova', 'sex': 'woman'},
        {'username': 'Maxim', 'surename': 'Zaitsev', 'sex': 'man'},
        {'username': 'Yulia', 'surename': 'Baranova', 'sex': 'woman'},
        {'username': 'Alexandra', 'surename': 'Yarovaya', 'sex': 'woman'}
    ]
}

simple_logger = logging.getLogger('Логгер для функции create_bd')
simple_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('file_name.log', mode='w', encoding='utf-8')
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(format)
simple_logger.addHandler(file_handler)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy()


class Schoolboy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60), nullable=False)
    surename = db.Column(db.String(60), nullable=False)
    sex = db.Column(db.String(60), nullable=False)
    group = db.Column(db.String(60), nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('school_direction.id'))

    def __repr__(self):
        return f'{self.user_name} {self.surename}'


class SchoolDirection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_faculty = db.Column(db.String, nullable=False)
    post = db.relationship('Schoolboy', backref='SchoolDirection', lazy=True)

    def __repr__(self):
        return self.name_faculty
