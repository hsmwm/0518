# -*- coding: utf-8 -*-
# @Time : 2020/6/4 3:42 下午
# @Author : zhl
# @File : lesson8.py
# @Software: PyCharm
# 2020-0603 - 异常处理作业
# 1. 异常捕获的语法是什么样的？    请列举你遇到过的/见过的错误类型。
'''
异常捕获的语法：
try:
    可能出错都代码块
except:
    '出错执行的代码'
    raise#返回异常信息
else:
    try里代码没有出错执行都代码
finally:
    无论是否出现一次都执行'

列举你遇到过的/见过的错误类型：
1，字符串索引超出范围
2，不支持在字符串和数字之间使用比较运算符
3，少参数
'''


# 2.编写如下程序
# 优化去生鲜超市买橘子程序
#
# a.收银员输入橘子的价格，单位：元／斤
#
# b.收银员输入用户购买橘子的重量，单位：斤
#
# c.计算并且 输出 付款金额
#
# 新需求：
#
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
#
try:
    price = float(input('请输入橘子的价格(元/斤)：'))
    weight = float(input('请输入橘子重量(斤)：'))
    money = price*weight
except:
    print('请检查输入是否为数字')
    raise
else:
    print(f'您选购的{price}元/斤的橘子,重{weight}kg,付款{money}')

def shop(price,weight):
    shop(price, weight)

# # import os
# # print(os.getcwd())
# print('d')