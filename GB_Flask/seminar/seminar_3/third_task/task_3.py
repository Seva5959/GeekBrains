from flask import Flask, render_template, request
from modles import db, User
from forms import RegisterForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_base_data.db'
db.init_app(app)

@app.cli.command('init')
def init_db():
    db.create_all()
    print('Database initialized!')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрированы!'
    return render_template('register.html', form=form)


@app.route('/users/')
def get_user():
    users = User.query.all()
    return f'{list(users)}'
