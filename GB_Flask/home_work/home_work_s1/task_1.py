# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для
# страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.


from flask import Flask, render_template
from data import pants_data, footwear_data, jacket_data

app = Flask(__name__)


@app.route('/')
def primary():
    return render_template('primary.html')


@app.route('/pants/')
def def_pants():
    return render_template('pants.html', pants=pants_data)


@app.route('/footwear')
def def_footwear():
    return render_template('footwear.html', foots=footwear_data)


@app.route('/jacket')
def def_jacket():
    return render_template('jacket.html', blazers=jacket_data)


app.run(debug=True)
