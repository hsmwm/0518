# -*- coding: utf-8 -*-
# @Time : 2020/6/7 10:54 下午
# @Author : zhl
# @File : lesson9.py
# @Software: PyCharm

# 1、类属性怎么定义？ 实例属性怎么定义？
'''
类属性定义:
直接定义在类中，不在任何实例方法中:如test_1
class Test1():
    test_1=9
''''''
实例属性：
self修饰
self.属性名使用
可使用__inti__()魔法函数定义

'''
# 2、实例方法中的self代表什么？（简答）
'''
答：实例对象本身
'''
# 3、类中__init__方法在什么时候会调用的？（简答）
'''
答：实例化对象时调用
'''
# 4、定义一个登录的测试用例类Case
# 属性：用例名称
# 用例步骤
# 预期结果
# 实际结果
# 方法：运行用例、用例结果(比对预期结果和实际结果是否相等)
# 实例化2个测试用例 ，并运行用例 ，呈现用例结果
# class Case:
#     def __init__(self,case_name,case_step,case_expected,case_actual):
#         self.case_name=case_name
#         self.case_step = case_step
#         self.case_expected = case_expected
#         self.case_actual=case_actual
#     def reult(self):
#         print(f'用例名{self.case_name},步骤{self.case_step},预期结果{self.case_expected}，实际结果{self.case_actual}')
# case1=Case('登录','输入正确用户名正确密码点击登录按钮','登录成功','登录成功')
# case2=Case('登录','输入正确用户名错误密码点击登录按钮','登录失败','登录失败')
# case1.reult()
# case2.reult()

#老师答案
class Case:
    user='xiaojian'
    passwd='123456'

    def __init__(self,case_name,case_user,case_pwd,case_expected):
        self.case_name = case_name
        self.case_user = case_user
        self.case_pwd=case_pwd
        self.case_expected = case_expected
        self.case_actual=None

    def run_case(self):
        print('运行测试用例')
        if self.user==self.case_user:
            self.case_actual='登录成功'
        else:
            self.case_actual='失败'
    def case_is_pass(self):
        if self.case_actual== self.case_expected:
            print('用例通过')
        else:
            print('用例失败')
case1=Case('登录成功','xiaojian','123456','登录成功')
case1.run_case()
case1.case_is_pass()
# 5、封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
# -  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
# 方法一：计算总分，
# 方法二：计算三科平均分，
# 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx, 性别：xxx。
# 实例化1个学生, 并打印学生个人信息，计算总分。
class Student:
    def __init__(self,identity,name,age,gender,English_score,math_score,Chinese_score):
        self.identity=identity
        self.name=name
        self.age=age
        self.gender=gender
        self.English=English_score
        self.math=math_score
        self.Chinese=Chinese_score
    def sum_score(self):
        return self.Chinese+self.English+self.math
    def avg_score(self):
        #return (self.Chinese+self.English+self.math)/3
        return self.sum_score()/3
    def print_info(self):
        print(f'我的名字是{self.name},年龄:{self.age},性别：{self.gender}')
#实例化学生
stu_1=Student('学生','wanganshi',18,'男',98,89,92)
#打印个人信息
stu_1.print_info()
#stu_1
print(f'总分为:{stu_1.sum_score()}')

