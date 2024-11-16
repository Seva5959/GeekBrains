from flask import Flask
from datetime import datetime
import re
from random import choice

app = Flask(__name__)
FILE_NAME = 'Sapogi_Chehov.txt'
DATA_CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']
DATA_CATS = ['корниш-рек', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counter = 0

def word_random(file_name: str) -> str:
    pattern = r'\b[а-яА-Я]{2,}\b'
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = f.read()
    all_word = re.findall(pattern, reader)
    return choice(all_word)


@app.route('/hello_world/')
def hw():
    return 'hello_world'


@app.route('/cars/')
def cars():
    return (', '.join(DATA_CARS))


@app.route('/cats/')
def cats():
    return (choice(DATA_CATS))


@app.route('/get_time/now/')
def get_time():
    return f'Current time: {datetime.now().strftime("%H:%M")}'


@app.route('/get_random_word/')
def get_random_word():
    return word_random(FILE_NAME)

@app.route('/counter/')
def counterkl():
    global counter
    counter += 1
    return str(counter)



app.run(debug=True)
