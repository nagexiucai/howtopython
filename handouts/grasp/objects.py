#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 以对象的眼光看待事物、部分语法和概念。

class Horse(object):
    '''
    as base class for horse family.
    '''

    def __init__(self, name, sex, age, address, order, *args, **kwargs):
        '''
        initialize a horse.
        '''
        self.name = name  # 名字
        self.sex = sex  # 性别
        self._age = age  # 年龄
        self._address = address  # 住址
        self.__order = order  # 次序

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

horse = Horse()
