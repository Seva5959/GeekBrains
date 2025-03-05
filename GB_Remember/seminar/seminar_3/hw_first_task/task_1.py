from flask import Flask, render_template
from models import SchoolDirection, SchoolBoy, db, simple_logger, students_data, sc_direction
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///information.db'
db.init_app(app)

def create_db():
    with app.app_context():
        if not os.path.exists('instance/information.db'):
            db.create_all()
            simple_logger.info('Созданы пустые таблицы')
            for name_fac in sc_direction:
                sc_dir = SchoolDirection(name_faculty=name_fac)
                db.session.add(sc_dir)
            for sc_dir in students_data:
                for people in students_data[sc_dir]:
                    educational = SchoolBoy(
                        name=people['username'],
                        surename=people['surename'],
                        sex=people['sex'],
                        group=sc_dir,
                        id_faculty=sc_direction[sc_dir])
                    db.session.add(educational)
                db.session.commit()
                simple_logger.info('База данных успешно заполнена')
            else:
                simple_logger.info('База данных уже существует')

@app.route('/')
def primary():
    create_db()
    educationals = SchoolBoy.query.all()
    return render_template('index.html', educationals=educationals)






















