#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 简述类的划分模式、部分Python语法和编程概念。

# 马类定义例程
# By Bob On 2017-09-13
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


# 狗类定义例程
# By Bob On 2017-09-20
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
