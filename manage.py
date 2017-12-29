# manage.py
from flask_script import Manager
from project import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
