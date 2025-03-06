from flask import Flask, render_template
from models import SchoolDirection, SchoolBoy, db, simple_logger, students_data, sc_direction
import os
simple_logger.info('4 строчка кода task_1') # удалить удалить удалить удалить удалить

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///information.db'
db.init_app(app)

def create_db():
    simple_logger.info('Функция create_db начала работу') # удалить удалить удалить удалить удалить
    with app.app_context():
        simple_logger.info('Контекстный менеджер открылся') # удалить удалить удалить удалить удалить
        if not os.path.exists('instance/information.db'):
            simple_logger.info('information.db не существует') # удалить удалить удалить удалить удалить удалить
            db.create_all()
            simple_logger.info('Созданы пустые таблицы') # удалить удалить удалить удалить удалить
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
                simple_logger.info('База данных успешно заполнена') # удалить удалить удалить удалить удалить
        else:
            simple_logger.info('База данных уже существует') # удалить удалить удалить удалить удалить

@app.route('/')
def primary():
    simple_logger.info('Функция primary начала работу') # удалить удалить удалить удалить удалить
    create_db()
    educationals = SchoolBoy.query.all()
    return render_template('index.html', educationals=educationals)






















