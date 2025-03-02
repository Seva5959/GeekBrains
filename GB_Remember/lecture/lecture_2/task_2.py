from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  # Обработчик для главной страницы
def home():
    return "Привет, это главная страница Flask!"
@app.route('/about/')
def about():
    con = {
        'title':'Обо мне',
        'name':'Всеволод',
        'age':'19'
    }
    return render_template('about.html', **con)

app.run(debug=True)