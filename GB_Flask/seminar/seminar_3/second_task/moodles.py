from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyBooks.db'

db = SQLAlchemy()


class Author(db.Model):
    id_au = db.Column(db.Integer, primary_key=True)
    name_au = db.Column(db.String(60), nullable=False)
    surname_au = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f'{self.name_au} {self.surname_au}'


class Book(db.Model):
    id_bk = db.Column(db.Integer, primary_key=True)
    name_bk = db.Column(db.String(60), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    authors = db.relationship('Author', secondary='book_author', backref='books', lazy=True)

    def __repr__(self):
        return f'{self.name_bk} ({self.year}), Copies: {self.count}'


book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id_bk'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id_au'), primary_key=True)
)
