# -*- coding: utf-8 -*-
# @Time : 2020/5/26 9:35 下午
# @Author : zhl
# @File : lesson4.py
# @Software: PyCharm
#
# 1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）
str1 = "hello xiao mi"
list1 = str1.split(' ')#字符串通过空格分割，返回列表list1['hello', 'xiao', 'mi']
list1.reverse()#列表list1通过反转返回['mi', 'xiao', 'hello']
str2 = list1[0]+' '+list1[1]+' ' +list1[2]#通过列表索引取出的字符串拼接为str2
print(str2)

# 2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
#         1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
personal = {}#定义空字典
personal['name'] = input('请输入姓名：')#获取用户输入
personal['gender'] = input('请输入性别：')#获取用户输入
personal['age'] = input('请输入年龄：')#获取用户输入
print(personal)
#         2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print(f"我的名字是{personal.get('name')}，今年{personal.get('gender')}岁，性别为{personal.get('age')}，喜欢敲代码")
print('我的名字是{}，今年{}岁，性别为{}，喜欢敲代码'.format(personal['name'],personal['gender'],personal['age']))
#         3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
add ={'height':180,'phone_number':'19103994994'}
personal.update(add)
print(personal)
#         4、平台为了保护你的隐私，需要你删除你的联系方式；
del personal['phone_number']
print(personal)
#         5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
personal['skill'] = '胸口碎大石'
print(personal)


# 3、利用下划线将列表li=[“python”,“java”,“php”]的元素拼接成一个字符串，然后将所有字母转换为大写，
#方法一
li = ["python","java","php"]
st1 = li[0]+'_'+li[1]+'_'+li[2]#获取列表元素并用下划线拼接为字符串st1
print(st1.upper())#st1.upper()对字符串进行大写转换并输出
#方法二：
st2 = '_'.join(li)
st3=st2.upper()
print(st3)

# 4、利用切片把 'http://www.python.org'中的python字符串取出来
#方法一：
str3 = 'http://www.python.org'
list2 = str3.split('.')#通过字符串分割获得list2:['http://www', 'python', 'org']
print(list2[1])#获取list2的第2个元素python
#方法二：
print(str3[str3.index('.')+1:-4])#直接运用字符串切片获取到python字符串


# 5、有下面几个数据 ，
# t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
# 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}
t1 = ("aa",11);t2= ("bb",22);li1 = [("cc",11)]
dict = {}#定义空字典
dict[t1[0]]=t1[1]#通过元组索引取值为字典添加元素
dict[li1[0][0]]=li1[0][1]#通过列表索引取值为字典添加元素
dict[t2[0]]=t2[1]#通过元组索引取值为字典添加元素
print(dict)
