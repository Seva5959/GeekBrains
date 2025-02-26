from flask import Flask, render_template
app = Flask(__name__)

@app.route('/about/')
def about():
    con = {
        'title':'Обо мне',
        'name':'Всеволод',
        'age':'19'
    }
    return render_template('about.html', **con)
