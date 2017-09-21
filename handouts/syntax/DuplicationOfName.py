#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/20 16:58
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 演示Python中的重名。

# START 同一个脚本中类重名

class A(object):
    __name__ = "Ai"
    __v__ = "i"
    v = "I"

print id(A), A.__name__, A.__v__, A.v

class A(object):
    __name__ = "Aii"
    __v__ = "ii"
    v = "II"

print id(A), A.__name__, A.__v__, A.v


A.__name__ = "modify it after defined"
print A.__name__

# TODO: 某些魔法是系统定义的（不能自定义）、只能在运行时重新赋值
# END 同一个脚本中类重名

# START 同一个类中方法重名

class B(object):
    @classmethod
    def b(cls):
        print "b for class"
    def b(self):
        print "b for instance"
    def b(self, x):
        print "b for instance with", x

# B.b()
b = B()
# b.b()
b.b("bb")

# TODO: 方法重名以最后定义的一个为准
