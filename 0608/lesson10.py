# -*- coding: utf-8 -*-
# @Time : 2020/6/10 2:21 下午
# @Author : zhl
# @File : lesson10.py
# @Software: PyCharm

# 1， 详细总结类和对象知识点，包括：
# 类的定义
'''
class 类名():
    属性
    方法（功能（函数））
'''
# 对象的初始化
'''
魔法方法__init__(self)可以实现对象初始化，创建对象时候自动调用。
'''
# 类属性
'''
类属性：直接定义在类中，不在任何实例方法中
'''
# 实例属性
'''
最好在初始化方法__init__(self)方法中实现
调用时self.属性名
'''
# 实例方法
'''
语法：
def 方法名(self):
    功能代码
实例调用
'''
# 类方法：
'''
@classmethod 声明类方法
语法：
@classmethod
def set_kind(cls):
  pass
其中cls代表当前类
可以访问类属性，但不能访问实例属性
'''
# 静态方法
'''
@staticmethod声明静态方法；与类无任何关系，是普通函数，只不过放类中，方便管理；类/实例均可访问静态方法
'''
# 继承
# 重写
'''
子类和父类有同名方法；子类重写方法完全不用父类内容
'''
# super 函数
'''
子类和父类有同名方法，且需要在父类基础上拓展内容；
'''
class Fruit():              #类定义
    kind='水果'                #定义类属性
    def __init__(self,color):
        self.color=color    #定义实例属性
    def can_eat(self):
        print('可以生吃')
    def can_plant(self):
        print('可以种植')     #定义实例方法

    @classmethod            #定义静态方法
    def test(cls):
        print(cls)
class Lemon(Fruit):         #定义子类继承父类Fruit
    def can_eat(self):      #父类方法完全重写
        print('可以泡水吃')
    def can_plant(self):
        super().can_plant()
        print('可以嫁接')     #父类方法用super重写

aa=Lemon('黄')
aa.test()   #实例调用静态方法
Lemon('黄').test()#类调用静态方法
print(aa.kind)#实例调用类属性



# 2， 定义一个类 Dog, 包含 2 个属性：名字和年龄。
# 定义一个方法 eat 吃东西。
# 定义一个类 TeddyDog, 继承 Dog 类， Teddy 在吃东西的时候还会望着你，  定义方法 watch_you.
# 定义一个类 BabyTeddyDog, 继承 TeddyDog,  BabyTeddy 吃东西不仅会望着你，还会四处转悠， 定义方法 go_around
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name,'吃东西')
class TeddyDog(Dog):
    def watch_you(self):
        self.eat()
        print(self.name,'望着你')
class BabyTeddyDog(TeddyDog):
    def go_around(self):
        self.watch_you()
        print(self.name,'转悠')
zhuli=TeddyDog('朱莉','3')
zhuli.watch_you()

xiaoli=BabyTeddyDog('小莉','1')
xiaoli.go_around()


# 二、选作题（不需要提交)
# 1.编写如下程序
# 编写一个工具箱类和工具类
#
# 工具类：需要有工具具的名称、功能描述、价格。
#
# 工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
#
#
#
# 实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
#
# 工具比如锤子、斧头、螺丝刀等工具。
#
# 提示：不需要用到继承。