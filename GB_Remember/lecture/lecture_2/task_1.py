from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/<path:file>/')
def get_file(file):
    return f'Ваш файл находиться в: {escape(file)}'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'Функция '
    return text

app.run(debug=True)
