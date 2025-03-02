from flask_sqlalchemy import SQLAlchemy

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


db = SQLAlchemy()

class SchoolBoy(db.Model):
    id_sb = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(10), nullable=False)

    direction_id = db.Column(db.Integer, db.ForeignKey('school_direction_id_sd'), nullable=False)
    direction = db.relationship('SchoolDirection', backref='disciple')
    grad = db.relationship('Grades', backref='grads')
    def __repr__(self):
        return f'{self.name} {self.surname}'

class SchoolDirection(db.Model):
    id_sd = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'Направление {self.name}'


class Grades(db.Model):
    id_g = db.Column(db.Integer,primary_key=True)
    learner_id = db.Column(db.Integer, db.ForeignKey('school_boy.id_sb'), nullable=False)
    learner = db.relationship('SchoolBoy', backref='learn')

    mathematics = db.Column(db.Integer, nullable=False)
    russian_language = db.Column(db.Integer, nullable=False)
    physical_culture = db.Column(db.Integer, nullable=False)
    direction_learner = db.Column(db.String, nullable=False)




