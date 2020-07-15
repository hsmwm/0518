# -*- coding: utf-8 -*-
# @Time : 2020/6/22 5:32 下午
# @Author : zhl
# @File : raad_yaml.py
# @Software: PyCharm

import yaml

with  open('nmb.yaml',encoding='utf-8') as fs:
    data   =yaml.load(fs,yaml.FullLoader)
    print(data)
