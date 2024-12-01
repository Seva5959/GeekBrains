from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 1


app.run(debug=True)
