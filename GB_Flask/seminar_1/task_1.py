from flask import Flask

app = Flask(__name__)
# Имена функций всегда должны быть разными !

@app.route('/')
def hello_world():  # Имена функций всегда должны быть разными !
    return 'Привет Незнакомец!'

@app.route('/Николай/')
def niko():
    return 'Привет Николай'

@app.route('/Олежа/')
@app.route('/Олег/')
@app.route('/Легенда/')
def oleg():
    return 'Привет Олег'

if __name__ == '__main__':
    app.run()