from werkzeug.security import generate_password_hash
from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from models import db, User
from forms import Valid_Auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_base_data.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init')
def db_init():
    db.create_all()
    print('OK')


@app.route('/', methods=["POST", "GET"])
def regis():
    form = Valid_Auth()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.confirm_password.data)
        user = User(name_us=name, surname_us=surname, email_us=email, password_us=password)
        db.session.add(user)
        db.session.commit()
        return render_template('succes.html', name=name, surname=surname)
    return render_template('index.html', form=form)


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)
