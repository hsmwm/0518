# -*- coding: utf-8 -*-
# @Time : 2020/6/16 3:39 下午
# @Author : zhl
# @File : about_ddt.py
# @Software: PyCharm

from ddt import ddt,data
import unittest

@ddt
class TestABC(unittest.TestCase):
    # @data(*[1,2],*[3,4])
    # def test_add(self,case):
    #     print('1111')
    #     print(case)

    @data(*{'name':'hsm','age':'10'}.items())
    def test_add(self, case):
        print('1111')
        print(case)

