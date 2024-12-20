from flask import Flask, render_template
from moodles import db, Author, Book
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyBooks.db'
db.init_app(app)


def init_db():
    db.create_all()
    print('OK')
    addst()


def addst():
    authors = []
    books = []

    # Создаём авторов
    for i in range(8):
        author = Author(name_au=f'Name_{i}', surname_au=f'Surname_{i}')
        authors.append(author)
        db.session.add(author)

    # Создаём книги
    for i in range(30):
        book = Book(name_bk=f'Book_{i}', year=1950 + i, count=random.randint(1, 100))
        books.append(book)
        db.session.add(book)

    db.session.commit()  # Сохраняем авторов и книги перед установкой связей

    # Устанавливаем связь "многие ко многим"
    for book in books:
        already_added_authors = set()  # Хранит id добавленных авторов для этой книги
        for _ in range(random.randint(1, 3)):  # Связываем с 1–3 авторами
            while True:
                author = random.choice(authors)
                if author.id_au not in already_added_authors:  # Проверка на уникальность
                    book.authors.append(author)
                    already_added_authors.add(author.id_au)
                    break

    db.session.commit()  # Сохраняем связи


@app.route('/')
def get_stedent():
    init_db()
    books = Book.query.all()
    return render_template('index.html', books=books)
