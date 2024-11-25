from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def def_main():
    if request.method == 'POST':
        user_name1 = request.form.get('username')
        user_email1 = request.form.get('auth_email')
        respon = make_response(redirect(url_for('hello')))
        respon.set_cookie('username',user_name1)
        respon.set_cookie('user_email',user_email1)
        return respon
    return render_template('index.html')

@app.route('/hello_user')
def hello():
    name = request.cookies.get('username')
    return render_template('hello_user.html', name=name)
 
@app.route('/logout')
def log():
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    resp.delete_cookie('user_email')
    return resp

app.run(debug=True)
