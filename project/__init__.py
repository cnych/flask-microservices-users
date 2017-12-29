import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# 初始化app
app = Flask(__name__)
# 环境配置
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# 初始化数据库
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
