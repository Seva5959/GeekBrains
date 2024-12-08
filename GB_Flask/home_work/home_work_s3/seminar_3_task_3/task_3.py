from flask import Flask, render_template, requests
from flask_wtf import CSRFProtect
from forms import ValidRegist
from modles import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET','POST'])
def auth():
    form = ValidRegist()
    if requests.method == 'POST' and form.validate():
        name = form.first_name.data
        surn = form.sure_name.data
        pasw = form.password_us.data
        login = form.login.data
        user = User(first_name=name,second_name=surn, login_us=login, password_us=pasw)
        db.session.add(user)
        db.session.commit()
        return f'Вы успешно зарегистрировались !'
    return render_template('index.html', form=form)

@app.route('/users')
def get_user():
    users = User.query.all()
    return f'{users}'

