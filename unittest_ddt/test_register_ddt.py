# -*- coding: utf-8 -*-
# @Time : 2020/6/15 3:30 下午
# @Author : zhl
# @File : test_register.py
# @Software: PyCharm


import unittest
from unittestapply.register import register
# import ddt
from unittestapply import myddt

datas=[{"title":"注册成功","user":"python38","passwd1":"lloommnn","passwd2":"lloommnn","check":{"code": 1, "msg": "注册成功"}},
       {"title":"所有参数不能为空","user":"","passwd1":"lloommnn","passwd2":"lloommnn","check":{"code": 0, "msg": "所有参数不能为空"}},
       {"title":"所有参数不能为空","user":"python38","passwd1":"","passwd2":"lloommnn","check":{"code": 0, "msg": "所有参数不能为空"}},
       {"title":"所有参数不能为空","user":"python38","passwd1":"lloommnn","passwd2":"","check":{"code": 0, "msg": "所有参数不能为空"}},
       {"title":"该账户已存在","user":"python26","passwd1":"lloommnn","passwd2":"lloommnn","check":{"code": 0, "msg": "该账户已存在"}},
       {"title":"两次密码不一致","user":"python38","passwd1":"lliii","passwd2":"lloommnn","check":{"code": 0, "msg": "两次密码不一致"}},
       {"title":"账号和密码必须在6-18位之间","user":"pytho","passwd1":"lloommnn","passwd2":"lloommnn","check":{"code": 0, "msg": "账号和密码必须在6-18位之间"}},
       {"title":"账号和密码必须在6-18位之间","user":"1234567890123456789","passwd1":"lloommnn","passwd2":"lloommnn","check":{"code": 0, "msg": "账号和密码必须在6-18位之间"}}]

@myddt.ddt
class TestRegister(unittest.TestCase):
    @myddt.data(*datas)
    def test_regist(self, case):
        # 1、测试数据
        # 2、测试步骤
        res =register(case["user"], case["passwd1"],case["passwd2"])
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res, case["check"])
    def setUp(self):
        print('=====用例执行开始=====')
    def tearDown(self):
        print('=====用例执行结束=====') #定义类方法 配置每个用例的前置后置条件