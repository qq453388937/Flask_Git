# -*- coding:utf-8 -*-
import redis


class Config:
    DEBUG = True
    SECRET_KEY = 'awdawdaefsfsf'
    SESSION_TYPE = 'redis'  # session 存储在redis
    PERMANENT_SESSION_LIFETIME = 3000
    SESSION_USER_SIGNER = True
    HOST = '127.0.0.1'
    PORT = 6379
    SESSIOIN_REDIS = redis.StrictRedis(host=HOST, port=PORT)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/flask_24'
    SQLALCHEMY_TRACK_MODIFICATIONS = True # 性能消耗
