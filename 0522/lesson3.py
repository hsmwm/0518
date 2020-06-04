print("{:*^30}".format('习题1'))
# 1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# 方法一：根据值删除
info.remove("矮穷丑")
# 方法二：根据索引删除
del info[3]
#方法三：pop()删除并返回删除的数据
info.pop(3)
print(info)

print("{:*^30}".format('习题2'))
# 2、现在有一个列表 li2=[1，2，3，4，5]，
# 请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]
li2 = [1,2,3,4,5]
#第一步用extend()合并列表
li3 = [11,22,33]
li2.extend(li3)
#第二步用inser()根据索引插入数据
li2.insert(3,66)
li2.insert(0,0)
print(li2)

print("{:*^30}".format('习题3'))
# 3、请写出删除列表中元素的方法。
#按值删除ls.remove()
#按索引删除del list[]
#按位删除，删除单个或多个ls.pop()
#ls.clear()
print('删除列表中元素方法需要掌握的有：\n方法一：按值删除ls.remove()\n方法二：按索引删除关键字：del \n方法三：删除并返回结果的ls.pop()\n方法四：清空列表ls.clear()')

print("{:*^30}".format('习题4'))
# 4、有5道小题（使用列表操作完成）：
# a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
personal = ['多么','女',18]
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
personal.append(170)
personal.append('17789899909')
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
personal.remove('17789899909')
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
personal.insert(1,'多么棒')
personal[4]='180'
# e, 你进一步添加自己的兴趣，至少需要 3 项(列表中成员可以是任意类型，此题考虑添加一个成员，且成员是列表哦！！！)。
interests = ['唱','跳','rap','篮球']
personal.append(interests)
print(personal)

