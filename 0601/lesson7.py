# # -*- coding: utf-8 -*-
# # @Time : 2020/6/1 11:26 下午
# # @Author : zhl
# # @File : lesson7.py
# # @Software: PyCharm
# 1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表），格式如下：
 #person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]
# 创建一个txt文本文件，来添加数据
# a.第一行添加如下内容：
# name,age,gender,hobby,motto
# b.从第二行开始，每行添加具体用户信息，例如：
# yuze,17,男,假正经, I am yours
# cainiao,18,女,看书,Lemon is best!
#列表内容
person_info =[{"name":"yuze", "age": '18', "gender": "男", "hobby": "假正经", "motto": "I am yours"},
              {"name":"wanger", "age": '22', "gender": "女", "hobby": "唱歌", "motto": "I am rapper "},
              {"name": "lisa", "age": '19', "gender": "女", "hobby": "舞蹈", "motto": "I am dancer "} ]
with open('test.txt',mode='w',encoding='UTF-8') as fs:#w模式打开test.txt,若文件不存在会新增，若文件存在会覆盖写入
    line=[]
    for key in person_info[0].keys():#获取列表第一个元素字典的key
        line.append(key+' ')#key和空格追加到列表中
    fs.writelines(line)#将列表写入文件
    fs.write('\n')#文件写入换行
    for i in person_info:#同样方法，循环获取列表中字典的values并添加到文件中，并每次换行
        line2 = []
        for j in i.values():
            line2.append(j)
        fs.writelines(line2)
        fs.write('\n')


# 编写如下程序
# 有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
#
# [{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]


#思路：从文件中逐行取出来，用@切割放入字典再追加到列表
def lesson7_2():
    with open('test2.txt',encoding='utf-8') as f:#上下文管理方式用默认只读方式打开文件
        result = []#创建结果的列表
        for i in f.readlines():#遍历文件内容，输出字符串
            list=i.strip('\n').split('@')#移除字符串后的\n,并将字符串根据@切割为列表
            dict = {}#创建空集合用于接收组装后的字典
            for j in range(len(list)):#遍历列表内容为组合集合
                dict[list[j][:list[j].index(':')]]=list[j][list[j].index(':')+1:]#对字符串进行切片，':'前作为key，':'后作为值
            result.append(dict)#字典追加到最终的列表中
        print(result)
lesson7_2()#调用函数

