# -*- coding: utf-8 -*-
# @Time : 2020/6/22 4:13 下午
# @Author : zhl
# @File : read_ini.py
# @Software: PyCharm

#from configparser import ConfigParser
#
# #实例化
# conf = ConfigParser()
# #读取配置文件记载到内存中
# conf.read('config.ini',encoding='utf-8')
# #读取某一项配置用：get
# value=conf.get('log','name')
# print(value)

from configparser import ConfigParser
import os

class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig(file_path)
    s=conf.get('log','name')
    print(s)