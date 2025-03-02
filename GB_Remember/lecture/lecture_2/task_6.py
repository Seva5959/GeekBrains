# Задание №6
# 📌 Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/cheak', methods=['POST', 'GET'])
def cheak():
    if request.method == 'POST':
        age = request.form.get('age')
        if int(age) < 18:
            return f'Нужно подождать еще {18-int(age)} лет'
        return render_template('seckret.html')
    return render_template('index.html')

app.run(debug=True)