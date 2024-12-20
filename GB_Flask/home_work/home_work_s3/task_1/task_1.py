from flask import Flask, render_template
from moodles import db, Schoolboy, SchoolDirection, students_data, sc_direction, simple_logger
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


def create_bd():
    with app.app_context():
        if not os.path.exists('instance/information.db'):
            db.create_all()
            simple_logger.info("Созданы пустые таблицы")
            for name_fac in sc_direction:  # sc_direction = dict
                sc_dir = SchoolDirection(name_faculty=name_fac)
                db.session.add(sc_dir)
            for sc_dir in (students_data):  # везде убрал enumerate
                for people in (students_data[sc_dir]):
                    educational = Schoolboy(
                        user_name=people['username'],
                        surename=people['surename'],
                        sex=people['sex'],
                        group=sc_dir,
                        id_faculty=sc_direction[sc_dir])
                    db.session.add(educational)
            db.session.commit()
            simple_logger.info("База данных успешно заполнена")
        else:
            simple_logger.info("База данных уже существует")


@app.route('/')
def primary():
    create_bd()
    educationals = Schoolboy.query.all()
    return render_template('index.html', educationals=educationals)
