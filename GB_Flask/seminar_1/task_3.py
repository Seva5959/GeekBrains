from flask import Flask

app = Flask(__name__)

data = '''<h1>Привет, меня зовут Алексей</h1> <p>Уже много лет я создаю сайты на Flask.
          <br/>Посмотрите на мой сайт.</p>'''


@app.route('/')
def hi():
    return 'Hello!'


@app.route('/text/')
def tcx():
    return data


@app.route('/poem/')
def poems():
    poem = [
        'Вот не думал, не гадал,',
        'Программистом взял и стал.',
        'Хитрый знает он язык,',
        'Он к другому не привык.',
    ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt

app.run(debug=True)
