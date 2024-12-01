from flask import Flask, render_template


from modles import db, Student, Faculty
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command('init-db') # Эта функция позволяет написать свою команду для терминала. Типо если написать flask --app 'путь к файлу ' 'имя функции'
def init_db():
    db.create_all()
    print('OK')

@app.cli.command('add_student')
def addst():
    for i in range(3):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)

    for i in range(8):
        stud = Student(
            username=f'name_{i}',
            surename=f'surename_{i}',
            sex=f'man' if i % 2 == 0 else 'woman',
            id_faculty = random.randrange(4),
            group=random.randrange(3)
        )
        db.session.add(stud)
    db.session.commit()
    print('Студенты добaвлены!')

