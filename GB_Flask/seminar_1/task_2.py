from flask import Flask
#38.10

app = Flask(__name__)

@app.route("/")
@app.route('/<name>/')
def hello(name='uncown'):
    return f'Hello, {name}!'


@app.route('/file/<path:file>/')
def set_path(file):
    return f'Путь до файла: {file}'


app.run()
