from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'

db = SQLAlchemy()

class Student(db.Model):
    id_s = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id_f'))

    def __repr__(self):
        return f'{self.username} {self.surname}'

class Faculty(db.Model):
    id_f = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return self.name
