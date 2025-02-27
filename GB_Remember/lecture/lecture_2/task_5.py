# Задание №5
# 📌 Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/math', methods=['POST','GET'])
def calk():
    if request.method == 'POST':
        oper = request.form.get('operation')
        int_1 = request.form.get('int_1')
        int_2 = request.form.get('int_2')
        if oper == '+':
            rez = int(int_1) + int(int_2)
        elif oper == '*':
            rez = int(int_1) * int(int_2)
        elif oper == '/':
            rez = int(int_1) / int(int_2)
        else:
            rez = int(int_1) - int(int_2)
        return render_template('rezult.html', rez=rez, int_1=int_1, int_2=int_2, oper=oper)
    return render_template('interface.html')

app.run(debug=True)
































