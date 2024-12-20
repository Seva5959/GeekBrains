from flask import Flask
from flask import render_template

app = Flask(__name__)

data = '''<h1>Привет, меня зовут Алексей</h1> <p>Уже много лет я создаю сайты на Flask.
          <br/>Посмотрите на мой сайт.</p>'''


@app.route('/')
def hi():
    return data


@app.route('/if/')
def show_if():
    context = {'title': 'Ветвление',
               'user': "Крутой хакер!",
               'number': 6}

    return render_template('show_if.html', **context)


app.run(debug=True)
