#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:27
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 把狗类共有的属性提升到一个基础狗类。

# 懒人的发现
# 新新Dog类
class Dog(object):
    Name = "dog"
    Sex = ""  # unknown
    Species = ""  # undetermined
    HairColor = ""  # unclear

    @classmethod
    def whatis(cls):
        print "it is a", cls.Sex, cls.Species, cls.HairColor, cls.Name

# 重新按性别划分
class DogClassifiedBySex(Dog):
    Sex = "undetermined"

DogClassifiedBySex.Sex = "male"
DogClassifiedBySex.whatis()

# 重新按品种划分
class DogClassifiedBySpecies(Dog):
    Species = "undetermined"

DogClassifiedBySpecies.Species = "city"
DogClassifiedBySpecies.whatis()
