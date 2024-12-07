from flask import Flask, render_template
from moodles import db, Schoolboy, SchoolDirection, students_data, sc_direction
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


def create_bd():
    with app.app_context():
        print("Данные подготовлены для записи.")
        if not os.path.exists('instance/information.db'):
            db.create_all()
            print("Данные подготовлены для записи.")
            for name_fac in sc_direction: # sc_direction -> dict
                sc_dir = SchoolDirection(name=name_fac)
                db.session.add(sc_dir)
            print("Данные подготовлены для записи.")
            for i, sc_dir in enumerate(students_data, start=1):
                for j, people in enumerate(students_data[sc_dir], start=1):
                    educational = Schoolboy(
                        user_name=people['username'],
                        surename=people['surename'],
                        sex=people['sex'],
                        group=sc_dir,
                        id_faculty=sc_direction[sc_dir])
                    db.session.add(educational)
            db.session.commit()
        else:
            print('База данных уже есть')


@app.route('/')
def primary():
    educationals = Schoolboy.query.all()
    return render_template('index.html', educationals=educationals)
