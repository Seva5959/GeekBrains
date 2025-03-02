from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/authorization', methods=['POST', 'GET'])
def auth():
    login = {'true_login': 'seva5959',
             'true_password': '1234'}

    if request.method == 'POST':
        user_email = request.form.get('user_email')
        user_passw = request.form.get('user_passw')
        if user_email == login['true_login'] and user_passw == login['true_password']:
            return 'Авторизация прошла успешно!'
        return render_template('mistake.html')
    return render_template('auth.html')


app.run(debug=True)
