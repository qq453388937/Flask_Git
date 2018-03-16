# -*- coding:utf-8 -*-

from flask import Flask, make_response, current_app, \
    request, session, jsonify, abort, redirect, url_for, \
    render_template, get_flashed_messages, flash
from flask_sqlalchemy import SQLAlchemy
# 导入配置文件
from settings import Config
# 导入wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import *
# 导入管理器对象
from flask_script import Manager
# 导入数据库迁移所用的类，命令类
from flask_migrate import Migrate, MigrateCommand



app = Flask(__name__)
app.config.from_object(Config)
# 导入蓝图对象用于注册
from _10_blueprint_splitagain import api
# 注册蓝图
app.register_blueprint(api)
db = SQLAlchemy(app)
# 迁移使用管理器对象 Manager(app)
# 迁移第一步
manager = Manager(app)
# 迁移第二步
migrate = Migrate(app, db)  # migrate 对象可以不定义
# 迁移第三部
manager.add_command('db', MigrateCommand)


# db = db.init_app(app)
# WTF 表单类，实例化表单对象，csrf
# 删除功能，在模板页中遍历数据，获取id 传给视图<int:id> 动态展示数据

# 定义模型类
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return 'author:%s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32))
    leader = db.Column(db.String(32))

    def __repr__(self):
        return 'book:%s' % self.info


class Form(FlaskForm):
    auth = StringField(validators=[DataRequired()], label=u'作者')
    book = StringField(validators=[DataRequired()], label=u'书籍')
    submit = SubmitField(label=u'添加')


@app.route('/', methods=['POST', 'GET'])
def author():
    form = Form()
    # 添加数据
    if form.validate_on_submit():
        wtf_auth = form.auth.data
        wtf_book = form.book.data

        auth = Author(name=wtf_auth)  # 直接通过命名参数给表的字段赋值
        book = Book(info=wtf_book)  # 直接通过命名参数给表的字段赋值

        # 存储
        db.session.add_all([auth, book])
        db.session.commit()
    all_auth = Author.query.all()
    all_book = Book.query.all()
    context = {
        'all_auth': all_auth,
        'all_book': all_book,
        'form': form,
    }

    # return render_template('author.html', all_auth=all_auth, all_book=all_book, form=form)
    return render_template('author.html', **context)


"""
try:
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
except:
    db.session.rollback()
    flash(******)
    abort()
"""

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # # 生成数据
    # au_xi = Author(name='我吃西红柿', email='xihongshi@163.com')
    # au_qian = Author(name='萧潜', email='xiaoqian@126.com')
    # au_san = Author(name='唐家三少', email='sanshao@163.com')
    # bk_xi = Book(info='吞噬星空', leader='罗峰')
    # bk_xi2 = Book(info='寸芒', leader='李杨')
    # bk_qian = Book(info='飘渺之旅', leader='李强')
    # bk_san = Book(info='冰火魔厨', leader='融念冰')
    # # 把数据提交给用户会话
    # db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # # 提交会话
    # db.session.commit()

    # app.run()

    # 迁移第四步骤
    print app.url_map
    manager.run()

"""
python _5db_select.py db init 第一次创建一次即可
python _5db_select.py db migrate -m 'init_tables_pxd注释注解' -m 可写可不写  
python _5db_select.py db upgrade
python _5db_select.py db history 查看历史迁移版本号码,根据guid版本号回退
python _5db_select.py db downgrade 4fc5046cb8c6 # 迁移回退直接会修改数据库 不建议回退
"""
