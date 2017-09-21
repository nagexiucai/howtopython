#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 简化的狗类定义。

# 狗类定义例程
class Dog(object):
    Name = "dog"  # 狗类共同的名字

    @classmethod
    def bark(cls):  # 狗类共同的叫喊声
        print "wang~wang!"

    @classmethod
    def wag(self):  # 狗类共同的摇尾巴
        print "whir~left~~whir~right"


# 因为分不出公母
class MaleDog(object):
    Name = "male dog"

class FemaleDog(object):
    Name = "female dog"


# 因为分不出品种
class CityDog(object):
    Name = "city dog"

class RuralDog(object):
    Name = "rural dog"
