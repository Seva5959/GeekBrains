from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from modles import db, SchoolDirection, SchoolBoy, Grades, sc_direction, students_data
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_base_data.db'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('init')
def init_bd():
    db.create_all()

def filing_bd():
    for name_dir in sc_direction:
        dire = SchoolDirection(name_sd=name_dir)
        db.session.add(dire)
    for sc_dir in students_data:
        for people in students_data[sc_dir]:
            educational = SchoolBoy(
                name_sb=people['username'],
                surname_sb=people['surename'],
                sex_sb=people['sex'],
                group=sc_dir,
                id_faculty=sc_direction[sc_dir])
            db.session.add(educational)
            grades_ed = Grades(
                learner_id=educational.id_sb,
                direction_learner=educational.direction.name_sd,
                mathematics=random.randrange(0,6),
                russian_language=random.randrange(0,6),
                physical_culture=random.randrange(0,6))
            db.session.add(grades_ed)
    db.session.commit()

def check_filing():
    if not SchoolDirection.query.first() and not SchoolBoy.query.first() and not Grades.query.first():
        filing_bd()

@app.route('/')
def primary():
    stud_infa = []
    check_filing()
    students = SchoolBoy.query.all()
    for student in students:
        stud_infa.append(student.name_sb)
        stud_infa.append(student.surname_sb)
        stud_infa.append(student.grad.mathematics)
        stud_infa.append(student.grad.russian_language)
        stud_infa.append(student.grad.physical_culture)
    return render_template('index.html', students=stud_infa)


