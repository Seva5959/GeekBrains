# Задание №4
# 📌 Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/sub', methods=['POST','GET'])
def sub():
    if request.method == 'POST':
        txt = request.form.get('user_txt')
        return render_template('counting.html', txt=txt, len_txt=len(txt))
    return render_template('main.html')

app.run(debug=True)