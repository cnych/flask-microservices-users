import unittest
from flask_script import Manager
from project import create_app, db
from project.api.models import User


app = create_app()
manager = Manager(app)


@manager.command
def recreate_db():
    """重新创建数据表."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """添加测试数据."""
    db.session.add(User(username='cnych', email="qikqiak@gmail.com"))
    db.session.add(User(username='chyang', email="icnych@gmail.com"))
    db.session.commit()


@manager.command
def test():
    """运行测试."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
