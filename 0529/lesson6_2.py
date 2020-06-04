# # # -*- coding: utf-8 -*-
# # # @Time : 2020/5/31 4:11 下午
# # # @Author : zhl
# # # @File : lesson6_2.py
# # # @Software: PyCharm
# # 2020-0529-函数操作练习题 - 祝大家周末愉快！！！
# # 1、定义函数：（要求：定义函数处理逻辑。input输入操作在函数之外。）
# # 将用户输入的所有数字相乘之后对20取余数
# # 用户输入的数字个数不确
#
#num = input('请输入一串数字，用逗号隔开')
#字符串分割为列表
# num= num.split(',')
# #定义函数
# def test1(*args):
#     result = 1
#     #循环获取列表元素乘积
#     for i in num:
#         result=int(i)*result
#     #获取与20取余数的值
#     print(result%20)
# test1(num)


#
# #
# # 2、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def test2(a):
    if len(a)>2:
        return a[0:2]
    else:
        print(a)
test2([1,4,6,6,0])
#
# # 3、列表去重
# # 定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# #方法一：新增空列表进行判断
# def remove_element(m_list):
#     m_list2 = []
#     for i in m_list:
#         if i not in m_list2:
#             m_list2.append(i)
#     print(m_list2)
# remove_element([10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1])#调用函数remove_element
# #方法二：运用集合特性
# def remove_element2(m_list):
#     print(list(set(m_list)))
# remove_element2([10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1])#调用函数remove_element2

# # 4、编写如下程序（要求：定义函数处理逻辑。input输入操作在函数之外。）
# # 尝试函数封装：
# # 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# # a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# # b.根据BMI指数，给与相应提醒
# # 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
# height = float(input('请输入身高（m）：'))
# weight = float(input('请输入体重（kg）：'))
# def BMI(height,weight):
#     bmi = weight/(height**2)
#     if bmi <18.5:
#         print('过轻')
#     elif 18.5<= bmi<25:
#         print('正常')
#     elif 25 <= bmi <28:
#         print('过重')
#     elif 28 <= bmi <32:
#         print('肥胖')
#     else:
#         print('严重肥胖')
# BMI(height,weight)
# # 5， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
# def test5(str,dic):
#     if str in dic.keys():
#         print('字典中存在该字符串的key')
#     else:
#         if str not in dic.values():
#             dic[str]=str
#             print(dic)
#         else:
#              print(f'字典中存在{str}的值')
# test5('dd',{'bb':' cc'})
#
# # 6， 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
# def test6(a,b):
#     x = int(input('请输入要做的操作：1加2减3乘4除：'))
#     if x==1:
#         y=a+b
#         print(y)
#     elif x==2:
#         y=a-b
#         print(y)
#     elif x==3:
#         y=a*b
#         print(y)
#     elif x==4:
#         y=a/b
#         print(y)
#     else:
#         print('不支持功能')
# test6(2,3)
#
#
#
#
# # 7， 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，
# # 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。(
# # （要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)
#分析：循环询问性别和年龄 询问10次，返回满足条件的人数
#定义
# count = []
# def test7(age,gender):
#     if (15<=age<=22 and gender=='女'):
#             count.append({gender:age})
#     else:
#          print('不符合条件')
#     print(count)
# #调用
# for i in range(10):
#    test7(age = int(input('输入年龄：')),gender =  input('输入性别：'))
# print(f'满足条件的总数为{len(count)}')