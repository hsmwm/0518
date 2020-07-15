# -*- coding: utf-8 -*-
# @Time : 2020/6/15 6:39 上午
# @Author : zhl
# @File : main_1.py
# @Software: PyCharm


import unittest

from unittest_case.test_lesson11 import TestLogin
from unittest_case.test_test11 import TestDome
#from HTMLTestRunner import HTMLTestRunner
# #实例话测试套件
# s=unittest.TestSuite()
# #添加一个用例addTest(类名('用例名'))
# s.addTest(TestLogin("test_login_ok"))
# #添加一个测试用例的列表 addTests([])
# s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_passwd")])
#

#从start_directory目录下开始搜索所有的测试用例并加载到测试套件中
#1，指定搜索目录
#2，文件过滤规则：以文件名匹配：test*.py
#3,在文件中过滤用例，继承unittest.TestCase类的测试类。类当中以test_开头的测试函数
s=unittest.TestLoader().discover(r"/Users/zhl/Documents/lenmon/lesson")
print(type(s))

#运行测试用例并生成结果testtxt
# runner = unittest.TextTestRunner()
# runner.run(s)

#创建HTML文件写的模式打开
# from HTMLTestRunnerNew import HTMLTestRunner
# with open('report.html','wb') as fs:
#     runner2 = HTMLTestRunner(fs,title='我的测试报告',tester='monica')
#     runner2.run(s)

#BeautifulReport
from BeautifulReport import BeautifulReport
br=BeautifulReport(s)
br.report('测试报告')

