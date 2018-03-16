# -*- coding:utf-8 -*-


from flask import Flask
from settings import Config
# 导入蓝图对象 因为注册使用蓝图对象
from _9goods_and_orders import api


app = Flask(__name__)
app.config.from_object(Config)

# 第三步注册蓝图对象到app上 , 延迟创建路由映射的原理
app.register_blueprint(api)


@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'


@app.route('/detail')
def detail():
    return 'detail'


if __name__ == '__main__':
    print app.url_map
    # 把拆分出去的goods_and_orders导入到当前文件中,循环导入,下放解决,交错导入
    # 也就是说模块化的制作形式,只能解决函数的调用问题,这里并不能解决路由映射的根本问题
    # from _9goods_and_orders import good, order

    app.run()
