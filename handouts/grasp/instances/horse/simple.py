#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/22 10:19
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 简化的马类实例化。

# 马类定义例程
class Horse(object):  # 定义名为Horse的类
    '''
    as base class for horse family.
    '''  # Horse的类文档
    Name = "horse"  # 定义名为Horse.Name的Horse的类变量

    @classmethod  # 类方法装饰器
    def clop(cls):  # 定义名为Horse.clop的一个自动参数的Horse的类方法
        '''
        sound of horse running.
        '''  # Horse.clop的方法文档
        print "clop~clop~"

    @classmethod
    def neigh(cls):
        print "nei~gh~~~"

    @classmethod
    def whatis(cls):
        print "it is a", Horse.Name

    # 马类实例初始化
    def __init__(self, name, sex, age, address, order):  # 定义名为__init__的一个自动参数和五个具名参数的Horse的实例方法
        '''
        initialize a horse.
        '''  # __init__的方法文档
        # Horse的实例的显式初始化属性清单
        self.name = name  # 名字
        self.sex = sex  # 性别
        self._age = age  # 年龄
        self._address = address  # 住址
        self.__order = order  # 次序

    def __tell_me_the_order(self):  # 定义名为__tell_me_the_order的隐藏的Horse的实例方法
        '''
        echo the order attribute of a horse object.
        '''  # __tell_me_the_order的方法文档
        print self.__order

    def _show_address(self):
        print self._address

    def change_name(self, name):
        self.name = name

    def run(self):
        self.stop = False  # 布尔假
        while not self.stop:
            Horse.clop()

    def stop(self):
        '''
        tell a horse to stop running.
        '''
        self.stop = True  # 布尔真

# horse = Horse("name", "sex", "age", "address", "order")
# horse.whatis()
# horse.run()

# 定义三匹马的马群
dilu = Horse("DiLu", "M", 7, "XuZhou", 001)
chitu = Horse("ChiTu", "M", 9, "JiZhou", 002)
wuzhui = Horse("WuZhui", "M", 8, "JinZhou", 003)

dilu.whatis()
chitu.whatis()
wuzhui.whatis()