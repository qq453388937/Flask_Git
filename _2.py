# -*- coding:utf-8 -*-
# 导入flask
from flask import Flask, make_response, current_app, request
# 导入配置文件
from settings import Config
# 导入转换器
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['POST'])
def demo1():
    return 'hello world1'


@app.route('/')
def demo2():  # 函数名不能重名
    return 'hello world2'


# 动态路由参数
@app.route('/<num>')
def demo3(num):
    return 'demo3:%s' % num


# 只能限制数据类型,不能限制数据长度
@app.route('/<int:num>')
def demo4(num):
    return 'demo4:%s' % num


@app.route('/<float:num>')
def demo5(num):
    # return 'demo5:%s' % num
    resp = make_response('demo5:%s' % num)
    return resp


# 自定义转换器
class Regex(BaseConverter):
    # regex = '[0-9]{5}' # 写死了
    def __init__(self, map, *args):
        super(Regex, self).__init__(map)
        # BaseConverter.__init__(map)
        self.regex = args[0]  # *args[0] 就是正则表达式
        print(type(map))
        print('----------------------')
        print(map)
        print(type(args))
        print(args)
        print('----------------------')


# 添加转换器到程序实例上
app.url_map.converters['re'] = Regex


@app.route('/d6/<re("[0-9]{5}"):suiyi>')  # re("..") ==> Regex("..")
def demo6(suiyi):
    return '---d6-%s---' % suiyi


# 优化原始静态访问地址
@app.route('/<re(".*"):filename>')
def demo7(filename):
    if not filename:
        filename = 'index.html'
    else:
        filename = 'html/' + filename
    # 把具体的文件返回给浏览器 make_response,current_app
    resp = make_response(current_app.send_static_file(filename))
    return resp


@app.route('/setcookie')
def demo8():
    resp = make_response('set cookie success')
    resp.set_cookie('user', 'python_24', max_age=5 * 60)
    return resp


@app.route('/getcookie')
def demo9():
    cookie = request.cookies.get('user')  # 和django大小写不一样
    return cookie if cookie else 'cookie啥也没有'  # 返回一个字符串 类似self.write()


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
