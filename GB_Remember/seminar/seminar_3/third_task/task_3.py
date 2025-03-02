from flask import Flask, render_template
from flask_wtf import CSRFProtect
from models import SchoolBoy, SchoolDirection, db, Grades, sc_direction, students_data
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_base_data.db'
db.init_app(app)
csrf = CSRFProtect

@app.cli.command('init')
def db_init():
    db.create_all()
    print('OK')

def filing_bd():
    for name_dir in sc_direction:
        dire = SchoolDirection(name=name_dir)
        db.session.add(dire)
    for sc_dir in students_data:
        for people in students_data[sc_dir]:
            educational = SchoolBoy(
                name=people['username'],
                surname=people['surename'],
                sex=people['sex'],
                group=sc_dir,
                direction_id=sc_direction[sc_dir])
            db.session.add(educational)
            db.session.flush()

            grades_ed = Grades(
                learner_id=educational.id_sb,
                direction_learner=educational.direction.name,
                mathematics=random.randrange(2, 6),
                russian_language=random.randrange(2, 6),
                physical_culture=random.randrange(2, 6))
            db.session.add(grades_ed)
    db.session.commit()


def check_filing():
    if not SchoolDirection.query.first() and not SchoolBoy.query.first() and not Grades.query.first():
        filing_bd()

@app.route('/')
def primary():
    stud_infa = {'name': [], 'surname': [], 'math': [], 'russ': [], 'phys': []}
    check_filing()
    students = SchoolBoy.query.all()
    for student in students:
        stud_infa['name'].append(student.name_sb)
        stud_infa['surname'].append(student.surname_sb)
        stud_infa['math'].append(student.grad[0].mathematics)
        stud_infa['russ'].append(student.grad[0].russian_language)
        stud_infa['phys'].append(student.grad[0].physical_culture)
    return render_template('index.html', students=stud_infa)


