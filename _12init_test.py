# -*- coding:utf-8 -*-

import unittest
from _6mail import *


class TestClass(unittest.TestCase):

    # 方法名称都为固定
    def setUp(self):
        """构造程序实例,构造客户端,制定配置信息"""
        self.app = app
        self.client = self.app.test_client()
        # self.db=db

    def tearDown(self):
        # db.session.remove() # 测试结束后要移除回话对象
        # db.drop_all()
        pass
    # 测试代码必须以test开头
    def test_xxx(self):
        resp = self.client.get('/')
        print(resp.data)
        # self.assertIsNotNone(...)
        self.assertEqual(resp.data, 'Sent  Succeed')
