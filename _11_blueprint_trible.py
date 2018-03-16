# -*- coding:utf-8 -*-
# 需要用到api 直接从10里面导过来无需重复创建api对象
from _10_blueprint_splitagain import api, Author, db, redirect, url_for


@api.route('/delete_auth<int:id>')
def delete_auth(id):
    # author = Author.query.get(id)
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('author'))
