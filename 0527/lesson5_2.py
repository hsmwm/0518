# # -*- coding: utf-8 -*-
# # @Time : 2020/5/29 12:56 下午
# # @Author : zhl
# # @File : lesson5_2.py
# # @Software: PyCharm
#
# 使用循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）

# 电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：

# 提示：电脑随机出拳
#
# 使用随机数，首先需要导入随机数的模块 —— “工具包”
#
# import random
#
# 导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
#
# random.randint(a, b)，返回[a, b]之间的整数，包含a和b
#
# random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
# random.randint(4, 4)  # 结果永远是 4
# random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
print('石头剪刀布游戏开始')
import random
print('请按下面提示出拳：\n石头【1】，剪刀【2】，布【3】，退出【4】')
game={1:'石头',2:'剪刀',3:'布'}
while True:
    my_choice = int(input('请输入你的选择'))
    compu = random.randint(1, 3)
    #   print(my_choice,compu)
    if my_choice == 4:
        print('你选择结束游戏，再见')
        break
    elif my_choice==compu:
        print('平局')
        continue
    elif (my_choice==1 and compu==2)or (my_choice==2 and compu==3) or (my_choice ==3 and compu == 1):
        print(f'我出{game[my_choice]},电脑是{game[compu]},我赢')
    else :
        print(f'我出{game[my_choice]},电脑是{game[compu]},我输')


# 2、编写如下程序
# a.用户输入1-7七个数字，分别代表周一到周日
#
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
#
# c.如果输入0，退出循环
#
# d.输入其他内容，提示：“输入有误，请重新输入！”
#
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

while True:
    num = int(input('输入数字1-7:'))
    dict={1:'一',2:'二',3:'三',4:'四',5:'五'}
    if num!=0:
        if num in dict.keys():
            print(f'今天是周{dict[num]}')
        elif num in [6,7]:
            print('周末')
        else:
            print('输入有误')
            continue
    else:
        break


#
#
#
#
#
#
#
# 3、冒泡排序（不要求提交，面试之前背熟）
#
#
# 使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
#
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法