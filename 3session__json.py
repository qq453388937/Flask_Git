# -*- coding:utf-8 -*-
# 导入flask
from flask import Flask, make_response, current_app, \
    request, session, jsonify, abort, redirect, url_for, render_template
# 导入配置文件
from settings import Config
# 导入转换器
from werkzeug.routing import BaseConverter
# 扩展包flask_sessionflask_session
from flask_session import Session
# json
import json

# flask_script 扩展包
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)

# 实例化管理器对象
manager = Manager(app)


@app.route('/str')
def str_test():
    return 'str'


@app.route('/set')
def set_session():
    session['name'] = 'python24'
    return 'set session ok'


@app.route('/get')
def get_session():
    resp = session.get('name', '没有session')
    return resp


@app.route('/json')
def json():
    my_dict = {"name": "aaa", "age": 30}
    return jsonify(my_dict)


@app.route('/status')
def demo():
    return 'demo', 500


@app.route('/err', methods=['GET'])
def demo2():
    abort(404)  # 只能抛出符合http协议的状态码,后面的代码不会执行类似python raise
    return 'demo', 302


# 自定义404错误页面 , 提高用户体验,404自定义,进入自定义后返回200 ok
@app.errorhandler(404)
def demo3(e):
    return '页面找不到了,请访问自定义页面%s' % e


@app.route('/red')
def red():  # 和flask函数不要重名
    return redirect('http://www.baidu.com')


@app.route('/red2')
def red2():
    return redirect(url_for('red'))


@app.after_request
def demo7(response):
    """在每次请求后运行"""
    # eg:修改响应头
    print(response)
    print('=========== after func run =============')
    response.headers['Content-Type'] = 'text;charset=utf-8;'
    return response  # 拿到response一定要返回


@app.before_first_request
def demo8():
    """在第一次请求运行"""
    print('第一次请求运行')


@app.before_request
def demo9():
    """每次请求前运行"""
    print('每次请求前运行')


@app.teardown_request
def demo10(response):
    """每次请求后运行"""
    print('每次请求后运行')
    return response


@app.route('/templ')
def templ_test():
    context = {'user': 'python24', 'age': 16}
    return render_template('index.html', context=context)


if __name__ == '__main__':
    print app.url_map
    # app.run(debug=True)
    manager.run()

""" python xxx.py runserver --help 
optional arguments:
  -?, --help            show this help message and exit
  -h HOST, --host HOST
  -p PORT, --port PORT
  --threaded
  --processes PROCESSES
  --passthrough-errors
  -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                        code)
  -D, --no-debug        disable the Werkzeug debugger
  -r, --reload          monitor Python files for changes (not 100{'const':
                        True, 'help': 'monitor Python files for changes (not
                        100% safe for production use)', 'option_strings':
                        ['-r', '--reload'], 'dest': 'use_reloader',
                        'required': False, 'nargs': 0, 'choices': None,
                        'default': None, 'prog': '3session__json.py
                        runserver', 'container': <argparse._ArgumentGroup
                        object at 0x7f33bc8d5d50>, 'type': None, 'metavar':
                        None}afe for production use)
  -R, --no-reload       do not monitor Python files for changes

"""