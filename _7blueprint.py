# -*- coding:utf-8 -*-

from flask import Flask

# 导入蓝图对象
from flask import Blueprint

# 把拆分出去的goods_and_orders导入到当前文件中
from _9goods_and_orders import good, order

api = Blueprint('api', __name__)


# 蓝图


@api.route('/list')
def list():
    return 'list'


@api.route('/list2')
def list2():
    return 'list2'
