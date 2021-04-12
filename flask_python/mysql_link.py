#ecoding=utf-8
# author:herui
# time:2021/4/12 9:55
# function:

from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/hrtest?charset=utf8mb4'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tmp_hello:ceshiren.com@182.92.129.158/tmp123?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    steps = db.Column(db.String(120), unique=False, nullable=True)


    def __repr__(self):
        return '<User %r>' % self.description

if __name__ == '__main__':
    db.session.add(TestCase(id=4, name="测试名称", description="描述测试", steps="step1"))
    db.session.commit()
