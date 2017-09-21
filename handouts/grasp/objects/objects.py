#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 以对象的眼光看待事物、部分Python语法和编程概念。

class Horse(object):
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

    def __init__(self, name, sex, age, address, order, *args, **kwargs):
        '''
        initialize a horse.
        '''
        self.name = name  # 名字
        self.sex = sex  # 性别
        self._age = age  # 年龄
        self._address = address  # 住址
        self.__order = order  # 次序
        self.multi_placeholder = args
        self.multi_key_value = kwargs

    def __tell_me_the_order(self):
        '''
        echo the order attribute of a horse object.
        '''
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

horse = Horse("name", "sex", "age", "address", "order")
horse.whatis()
horse.run()
