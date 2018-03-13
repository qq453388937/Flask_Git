# -*- coding:utf-8 -*-
import redis


class Config:
    DEBUG = True
    SECRET_KEY = 'awdawdaefsfsf'  # csrf也会用到
    SESSION_TYPE = 'redis'  # session 存储在redis
    PERMANENT_SESSION_LIFETIME = 3000
    SESSION_USER_SIGNER = True
    HOST = '127.0.0.1'
    PORT = 6379
    SESSIOIN_REDIS = redis.StrictRedis(host=HOST, port=PORT)
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/flask_24'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/a3'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/iii'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 性能消耗
    SQLALCHEMY_ECHO = True  # 展示SQL语句
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 请求过程中自动提交数据无需手动commit
