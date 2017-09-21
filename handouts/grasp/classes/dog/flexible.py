#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:24
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 避免每种狗都定义一个类这种繁琐状况的办法。

# 理论上可以给每一种狗定义一个类太繁琐
# 重新定义狗：把一些特征放在类变量
class Dog(object):
    Name = "dog"
    Sex = "unknown"
    Species = "undetermined"
    HairColor = "unclear"

    @classmethod
    def whatis(cls):
        print "it is a", Dog.Sex, Dog.Species, Dog.HairColor, Dog.Name

# male city white
Dog.Sex = "male"
Dog.Species = "city"
Dog.HairColor = "white"
Dog.whatis()

# female rural black
Dog.Sex = "female"
Dog.Species = "rural"
Dog.HairColor = "black"
Dog.whatis()

# 按性别划分狗
class DogClassifiedBySex(object):
    Name = "dog"
    Sex = "undetermined"
    Species = ""  # whatever
    HairColor = ""  # no-matter

    @classmethod
    def whatis(cls):
        print "it is a", DogClassifiedBySex.Sex, DogClassifiedBySex.Species, DogClassifiedBySex.HairColor, DogClassifiedBySex.Name

DogClassifiedBySex.Sex = "male"
DogClassifiedBySex.whatis()
DogClassifiedBySex.Sex = "female"
DogClassifiedBySex.whatis()

# 按品种划分狗
class DogClassifiedBySpecies(object):
    Name = "dog"
    Sex = ""  # whatever
    Species = "undetermined"
    HairColor = ""  # no-matter

    @classmethod
    def whatis(cls):
        print "it is a", DogClassifiedBySpecies.Sex, DogClassifiedBySpecies.Species, DogClassifiedBySpecies.HairColor, DogClassifiedBySpecies.Name

DogClassifiedBySpecies.Species = "city"
DogClassifiedBySpecies.whatis()
DogClassifiedBySpecies.Species = "rural"
DogClassifiedBySpecies.whatis()
