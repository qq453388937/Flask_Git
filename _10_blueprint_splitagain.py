# -*- coding:utf-8 -*-

# 可以从_5db_select 里面导入,也可以从FLask导入.都可以!
from flask import Blueprint


api = Blueprint('api', __name__)

# 这里可以下放,交错导入
from _5db_select import Author, Book, db, redirect, url_for, app, flash, abort
# 关联第三个文件 这个可以无限下放只要注册了就可以
"""注意再次拆分出去的文件需要把文件再次导入到创建蓝图实例文件中的地方追加注册"""
from _11_blueprint_trible import delete_auth


# @api.route('/delete_auth<int:id>')
# def delete_auth(id):
#     # author = Author.query.get(id)
#     author = Author.query.filter_by(id=id).first()
#     db.session.delete(author)
#     db.session.commit()
#     return redirect(url_for('author'))


@api.route('/delete_book<int:id>')
def delete_book(id):
    book = Author.query.filter_by(id=id).first()
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash('出错了')
        abort(500)
    return redirect(url_for('author'))
