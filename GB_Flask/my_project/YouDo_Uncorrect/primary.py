from form import ValidForm
from models import Authorization, db
from flask import Flask, request, render_template
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('init')
def init_db():
    db.create_all()
    print('OK')

@app.route('/',methods=['POST','GET'])
def regis():
    form = ValidForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password_confirm.data
        auth = Authorization(name=name, surname=surname, password=password, email=email)
        db.session.add(auth)
        db.session.commit()
        return render_template('task.html',name=name)
    return render_template('main_page.html', forms=form)





