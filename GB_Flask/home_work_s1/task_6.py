from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<int:num_1>/<int:num_2>/')
def lenght(num_1, num_2):
    return f'{num_1 / num_2 =  }'


@app.route('/table/')
def table():
    head = {
        'firstname': 'Имя',
        'lastname': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'}

    student_last = [{
        'firstname': 'Имя_1',
        'lastname': 'Фамилия_1',
        'age': '89',
        'rating': '3.2'},
        {
            'firstname': 'Имя_2',
            'lastname': 'Фамилия_2',
            'age': '21',
            'rating': '4.3'},
        {
            'firstname': 'Имя_3',
            'lastname': 'Фамилия_3',
            'age': '23',
            'rating': '4.65'}]

    return render_template('base.html', head=head, student_last=student_last)


app.run(debug=True)
