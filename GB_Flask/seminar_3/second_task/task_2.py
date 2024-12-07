from flask import Flask, render_template
from moodles import db, Author, Book, BookAuthor
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyBooks.db'
db.init_app(app)


@app.cli.command('qw')
def init_db():
    db.create_all()
    print('OK')
    addst()


def addst():
    for i in range(30):
        book = Book(name_bk=f'faculty_{i}',
                    year=1950 + i,
                    count=random.randrange(30, 25000))
        db.session.add(book)

    for i in range(8):
        author = Author(
            name_au=f'name_{i}',
            surname_au=f'surename_{i}',
        )
        db.session.add(author)

    for i in range(30):
        book_author = BookAuthor(
            book_id=random.randrange(30),
            author_id=random.randrange(15))
        db.session.add(book_author)
    db.session.commit()


@app.route('/')
def get_stedent():
    init_db()
    author_infa = Author.query.all()
    return render_template('index.html', author=author_infa)
