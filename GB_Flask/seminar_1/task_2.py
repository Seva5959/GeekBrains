from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route('/<name>/')
def hello(name='uncown'):
    return f'Hello, {name}!'


@app.route('/file/<path:file>/')
def set_path(file):
    return f'Путь до файла: {file}'

@app.route('/number/<int:num>/')
def dig(num):
    return f'Передано число {num}'

app.run()
