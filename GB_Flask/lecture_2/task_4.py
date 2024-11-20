from pathlib import PurePath, Path
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


# загружаем файл у пользователя в папку uploads

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


app.run(debug=True, port=5001)
