from flask import Flask, request, render_template

app = Flask(__name__)

@app.get('/submit')
def sub_get():
    return render_template('form.html')

@app.post('/submit')
def sub_post():
    name = request.form.get('name')
    return f'Hello {name}!'

app.run(debug=True)