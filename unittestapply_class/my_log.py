# -*- coding: utf-8 -*-
# @Time : 2020/6/19 5:35 下午
# @Author : zhl
# @File : my_log.py
# @Software: PyCharm

import logging


class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        super().__init__(name, level)

        #设置日志格式
        formt='%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter=logging.Formatter(formt)

        #控制台渠道输出
        handle1=logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)
        #文件渠道输出
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


logger = MyLogger("py30", file="my_logger.log")

if __name__ == '__main__':
    mlogger = MyLogger("py30", file="my_logger.log")
    mlogger.info("我的日志类")