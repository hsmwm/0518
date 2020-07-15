# -*- coding: utf-8 -*-
# @Time : 2020/6/15 3:30 下午
# @Author : zhl
# @File : test_register.py
# @Software: PyCharm

import unittest
from unittestapply.register import register
from unittestapply.myddt import ddt,data
from openpyxl import load_workbook
import os


file_path= os.path.join(os.path.dirname(os.path.abspath(__file__)),'unittest_excel.xlsx')#应用os包中的函数得到excel所在路径
wb = load_workbook(file_path)#加载excel文件
sh = wb['regist']#定位表单

all_datas=[] #用来装所有的测试数据的列表
titles = [] #用来装第一行的列表
#遍历第一行数据
for title in list(sh.rows)[0]:
    titles.append(title.value)#追加到titles列表中

# 遍历除第一行以外的数据
for item in list(sh.rows)[1:]:#遍历行
    values = []
    for val in item:
        values.append(val.value)#获取的值追加到列表
    res = dict(zip(titles,values))  # zip将第一行和每其他数据打包成字典
    res["check"] = eval(res["check"])  # 将check的字符串，转换为字典对象。
    all_datas.append(res) # 追加到all_datas列表

#测试数据 测试步骤 断言 ddt
@ddt
class TestRegister(unittest.TestCase):

    @data(*all_datas)
    def test_login(self, case):
        res = register(case["user"], case["passwd1"],case["passwd2"])
        self.assertEqual(res, case["check"])
