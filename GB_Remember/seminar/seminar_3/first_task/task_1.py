from flask import Flask, render_template
from models import db, Faculty, Student
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Таблицы созданы')

@app.cli.command('add_student')
def addst():
    for i in range(3):
        faculty = Faculty(name=f'факультет_№{i}')
        db.session.add(faculty)

    for i in range(8):
        stud = Student(
            username=f'имя_№{i}',
            surname=f'фамилия_№{i}',
            sex='man' if i // 2 == 0 else 'woman',
            id_faculty=random.randrange(4),
            group=random.randrange(3)
        )
        db.session.add(stud)
    db.session.commit()
    print('Студенты добавлены!')


@app.route('/')
def get_stydent():
    students_infa = Student.query.all()
    return render_template('index.html', students_infa=students_infa)




