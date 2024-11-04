from flask import Flask, request, render_template

app = Flask(__name__)


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit') # Разделение нужно для безопасности данных
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


app.run(debug=True, port=5001)
