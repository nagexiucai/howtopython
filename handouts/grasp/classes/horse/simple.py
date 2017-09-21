#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 简化的马类定义。

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

Horse.whatis()
Horse.clop()
Horse.neigh()
