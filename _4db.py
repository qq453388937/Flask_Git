# -*- coding:utf-8 -*-
from flask import Flask
# 导入flask——sqlalchemy 扩展包
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# 创建SQLALchemy对象
db = SQLAlchemy(app)


# db = SQLAlchemy()
# app = db.init_app(app)

# 定义模型类

class Role(db.Model):
    # 表名称可以不定义，默认创建是同类名的表名，但不是复数
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    us = db.relationship('User', backref='role')

    # 输出数据库查询字符串
    def __repr__(self):
        return '%s' %self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


if __name__ == '__main__':
    # 删除所有表
    db.drop_all()
    # 代码创建表
    db.create_all()
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1, ro2])
    db.session.commit()
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    app.run()
