# -*- coding:utf-8 -*-
from flask import Flask
# 导入flask——sqlalchemy 扩展包
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

# 创建SQLAlchemy对象
db = SQLAlchemy(app)


# db = SQLAlchemy()
# app = db.init_app(app) # 两种实例化SQLAlchemy


# 定义模型类
class Role(db.Model):
    # 表名称可以不定义，默认创建是同类名的表名，但不是复数
    __tablename__ = 'roles'
    # 字段名 = db.Column(字段类型，约束)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # relationship 第一个参数是多方的类名
    # backref是user对象反向找回点回来的名称，us是正向找多个的点的名称
    # .us 实现一对多，.role实现多对一
    us = db.relationship('User', backref='role')

    # 自定义输出数据库查询字符串.all()显示什么
    def __repr__(self):
        """自定义输出数据库查询字符串
        ipython终端导入之后会缓存要重新进入，进入ipython一定要在虚拟环境下进入
        """
        return '%s:zidiyi:%s' % (self.id, self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键   db.ForeignKey('表名.id')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def select_practice():
    import json
    all_role = Role.query.all()  # 模型只有一个字段会返回一个列表而不是对象
    all_user = User.query.all()
    # return str(all_user[0].email)
    one_role = Role.query.get(1)
    one_user = User.query.get(5)
    from sqlalchemy import and_,or_,not_
    #
    #
    """
    User.query.filter_by(name='chen').first().name
    User.query.filter_by(name='chen')[0].name
    User.query.filter_by(name='chen').all()
    User.query.filter(User.name=='chen').all()
    User.query.filter(Role.name=='admin').all() 关联查询
    User.query.filter(User.name != 'pxd').all()
    User.query.filter(and_(User.name=='wang',User.email.endswith('1633.com'))).first().name
    User.query.filter(or_(User.name=='wang',User.email.endswith('1633.com'))).first().name
    User.query.filter(not_(User.name=='wang')).all()
    role = Role.query.first()
    role.us 看多少人是管理员
    user = User.query.first()
    user.role
    
    User.query.filter_by(name='pxd').update({'name':'ddd','pswd':'qq2921481'})
    User.query.filter(User.name=='pxd').update({'name':'ddd','pswd':'qq2921481'})
    
    user = User.query.first()
    db.session.delete(user)
    db.session.commit()
    """

    print(one_role.id, one_role.name)
    return 'ok'


if __name__ == '__main__':
    print(app.url_map)
    # # 删除所有表
    # db.drop_all()
    # # 代码创建表
    # db.create_all()
    # ro1 = Role(name='admin')
    # ro2 = Role(name='user')
    # # db.session.add() # 添加一条数据
    # db.session.add_all([ro1, ro2])
    # db.session.commit()
    # us1 = User(name='wang', email='wang@1633.com', pswd='123456', role_id=ro1.id)
    # us2 = User(name='zhang', email='zhang@1893.com', pswd='201512', role_id=ro2.id)
    # us3 = User(name='chen', email='chen@1263.com', pswd='987654', role_id=ro2.id)
    # us4 = User(name='zhou', email='zhou@1633.com', pswd='456789', role_id=ro1.id)
    # db.session.add_all([us1, us2, us3, us4])
    # db.session.commit()
    app.run()
