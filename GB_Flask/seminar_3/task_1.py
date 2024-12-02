from flask import Flask, render_template


from modles import db, Student, Faculty
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command('init-db') # Эта функция позволяет написать свою команду для терминала. Типо если написать flask --app 'путь к файлу ' 'имя функции'
def init_db():
    # Эта функция инициализирует таблицы, но если они уже существовали, но она ничего не делает
    db.create_all()
    print('OK')
    # В этой функции мы не используем сессии, так как эта функция просто создает ТАБЛИЦЫ. Она НЕ трогает ДАННЫЕ.

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
    # Сессии нужны ((( Без них к сожалению нельзя добавить данные. По сути они работают как git.
    # Все что нужно добавляй (правда git add . нет), а в конце нужно сделать коммит
    print('Студенты добaвлены!')

@app.route('/')
def get_stedent():
  # students_infa = Student.query.first() Позволил бы получить только первую запись из таблицы Student, иначе вернет None
    students_infa = Student.query.all() # позволяет получить все записи из таблицы Student
    return render_template('index.html', students=students_infa)
