from pathlib import PurePath, Path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/next')
def next_page():
    return ('Hello, Oleg!')


@app.route('/load_image', methods=['GET', 'POST'])
def load_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'file {escape(file_name)} successfully uploads on server!'
    context = {'task': 'Задание №2'}
    return render_template('page_2.html', **context)


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    login = {'auth_email': 'aboba@gmail.com',
             'auth_pasw': '1234'}
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pasw = request.form.get('auth_pasw')
        if auth_email == login['auth_email'] and auth_pasw == login['auth_pasw']:
            return f'Authorization {auth_email} make successfully!'
        else:
            return 'You make mistake password or email!'
    context = {'task': 'Задание №3'}
    return render_template('authorization.html', **context)


@app.route('/writeline', methods=['GET', 'POST'])
def writeline():
    txt = request.form.get('text')
    context = {'task': 'Задание №4',
               'count': f'{len(txt) if txt else 0}'}
    return render_template('writeline.html', **context)


@app.route('/mathematics', methods=['GET', 'POST'])
def mathematics():
    final_number = 0
    if request.method == "POST":
        num_1 = int(request.form.get('num_1',0))
        num_2 = int(request.form.get('num_2',0))
        oper = request.form.get('oper','+')
        if oper == '+':
            final_number = num_1 + num_2
        elif oper == '-':
            final_number = num_1 - num_2
        elif oper == '*':
            final_number = num_1 * num_2
        elif oper == '/':
            final_number = num_1 / num_2

    context = {'task': 'Задание №5',
               'final_number': final_number}
    return render_template('mathematics.html', **context)



app.run(debug=True)
