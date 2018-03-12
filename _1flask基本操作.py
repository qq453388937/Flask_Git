# coding:utf-8
from flask import Flask
from settings import *
from werkzeug.routing import BaseConverter

# app.config['DEBUG'] = True

app = Flask(__name__)
# app.config.from_object(Config)
# app = Flask('__main__')
"""werkzeug"""


# 只能限制数据类型,不能限制数据长度
@app.route('/<int:num>')  # <float:num>
def demo3(num):
    print(type(num))
    return 'demo:%s' % num


@app.route('/')
def hello_world2():
    return 'hello world222'


@app.route('/', methods=['POST'])
def hello_world():
    return 'Hello World111!'  # help('modules')


if __name__ == '__main__':
    print app.url_map

    app.run(debug=True)
