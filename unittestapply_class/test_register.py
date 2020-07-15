# -*- coding: utf-8 -*-
# @Time : 2020/6/15 3:30 下午
# @Author : zhl
# @File : test_register.py
# @Software: PyCharm

import unittest
from unittestapply.register import register
from unittestapply.myddt import ddt,data
from unittestapply_class.handle_excel import HandleExcel
import os
from unittestapply_class.my_log_2 import logger
#from unittestapply_class.my_log import logger

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'unittest_excel_class.xlsx')  # 应用os包中的函数得到excel所在路径
ex = HandleExcel(file_path, 'regist')
cases = ex.read_all_datas()
ex.close_file()


#测试数据 测试步骤 断言 ddt logger
@ddt
class TestRegister(unittest.TestCase):
    @data(*cases)
    def test_login(self, case):
        logger.info("************* 开始执行测试用例 ****************")
        logger.info("测试数据：{}".format(case))
        res = register(case["user"], case["passwd1"], case["passwd2"])
        logger.info("实际运行结果为：{}".format(res))
        try:
            self.assertEqual(res, eval(case["check"]))
        except AssertionError:
            logger.exception("断言失败：用例Fail！")
            raise
        else:
            logger.info("断言成功，用例Pass！")
        logger.info("***********  测试用例执行结束 **************")

