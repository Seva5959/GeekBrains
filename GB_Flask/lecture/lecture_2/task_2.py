from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Всеволод',
    'age': 18}

    return render_template('about.html', **context) # **context нужен для того, чтобы распаковать словарь


app.run(debug=True, port=5001)
