# -*- coding:utf-8 -*-
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
# 配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.163.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,  # 传输协议
    MAIL_USERNAME='15346566750@163.com',
    MAIL_PASSWORD='wy2921481',
)
# app.config.update(
#     DEBUG=True,
#     MAIL_SERVER='smtp.qq.com',
#     MAIL_PROT=465,
#     MAIL_USE_TLS=True,
#     MAIL_USERNAME='453388937@qq.com',
#     MAIL_PASSWORD='vpbycoqspbzsbgfb',
# )

mail = Mail(app)

from _7blueprint import api

app.register_blueprint(api)  # 可以单独出去使用，可以拆分模块出去，但是不能再flask模块里使用


@app.route('/')
def index():
    # sender 发送方，recipients 接收方列表
    msg = Message("never give up ", sender='15346566750@163.com', recipients=['453388937@qq.com', ])
    msg.body = "<h1>flask is good!</h1>"
    # 发送邮件
    mail.send(msg)
    print "Mail sent"
    return "Sent Succeed"


if __name__ == "__main__":
    print(app.url_map)
    app.run()
