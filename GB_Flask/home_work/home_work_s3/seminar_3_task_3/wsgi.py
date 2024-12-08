from task_3 import app
from modles import db

if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)


