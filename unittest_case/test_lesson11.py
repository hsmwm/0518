# -*- coding: utf-8 -*-
# @Time : 2020/6/12 10:17 上午
# @Author : zhl
# @File : test_lesson11.py
# @Software: PyCharm

"""
定义测试类，继承unittest.TestCase
在测试类中以test_开头，定义测试函数
每个以test_开头的函数就是测试用例
编写用例：
    1。测试数据
    2。测试步骤
    3，断言预期结果与实际结果的比对
        AssertionError:断言失败-用例失败
        assert 表达式（True表示通过）
"""
import unittest
from unittest_case.login import login_check
import ddt
datas=[{"user":"python27","passwd":"lemonban","check":{"code": 0, "msg": "登录成功"}},
    {"user":"python27","passwd":"lemonban11","check":{"code": 1, "msg": "账号或密码不正确"}},
    {"user":"python25","passwd":"lemonban","check":{"code": 1, "msg": "账号或密码不正确"}}]
@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('1')
    @classmethod
    def tearDownClass(cls):
        print('2')
    def setUp(self):
        print('a')
    def tearDown(self):
        print('b')
    @ddt.data(*datas)
    def test_login(self, case):
        # 1、测试数据 # 2、测试步骤
        res = login_check(case["user"], case["passwd"])
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res, case["check"])

# def test_login_ok(self):
    #     res = login_check("python27","lemonban")
    #     self.assertEqual(res,({"code": 0, "msg": "登录成功"}))
    # def test_login_wrong_passwd(self):
    #     res= login_check("python27","lemonban1")
    #     self.assertEqual(res, ({"code": 1, "msg": "账号或密码不正确"}))
    # def test_login_wrong_user(self):
    #     res = login_check("python28", "lemonban")
    #     self.assertEqual(res, ({"code": 1, "msg": "账号或密码不正确"}))
    # def test_login_no_passwd(self):
    #     res = login_check("python27")
    #     self.assertEqual(res, ({"code": 1, "msg": "所有的参数不能为空"}))
    # def test_login_no_user(self):
    #     res = login_check( "lemonban")
    #     self.assertEqual(res, ({"code": 1, "msg": "所有的参数不能为空"}))