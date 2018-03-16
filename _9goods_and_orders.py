# -*- coding:utf-8 -*-

# 把8实例化的app 导入进来 # 这个已经无法下放交错导入 注意,当使用蓝图对象的时候就不需要main当中的app了
# from _8blueprint_main import app
# 1.导入蓝图模块
from flask import Blueprint
# 2.定义蓝图对象
# 可以写在单个独立的脚本文件中,也可以在拆分出去的模块当中使用,但是不可以在创建FLASK实例的地方使用
api = Blueprint('api', __name__, url_prefix='/v1.0')  # api 习惯和name 相同便于区分,url中RESTFul风格带版本号


@api.route('/good')
def good():
    return 'goods'


@api.route('/order')
def order():
    return 'order'
