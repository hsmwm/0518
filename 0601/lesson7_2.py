# -*- coding: utf-8 -*-
# @Time : 2020/6/2 1:52 下午
# @Author : zhl
# @File : lesson7_2.py
# @Software: PyCharm

num_list = [100,2,3,4]
def add(a,b,c,d):
    sum_num=a+b+c+d
    print(sum_num)
    return sum_num
add(*num_list)


def print_info(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
person_info={'name':'z','age':20,'city':'shanghai'}
print_info(**person_info)