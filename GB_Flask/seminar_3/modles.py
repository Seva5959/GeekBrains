from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    surename = db.Column(db.String(120),nullable=False)
    sex = db.Column(db.String(80),nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    def __repr__(self):
        return f'{self.username} {self.surename}'

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    posts = db.relationship('Students', backref='faculty', lazy=True)


    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    def __repr__(self):
        return f'{self.name}'
