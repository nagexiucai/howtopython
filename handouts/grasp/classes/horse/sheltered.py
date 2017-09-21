#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:30
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 尝试隐藏一些马类的敏感属性。

# 有些属性不想曝光
# 重新定义马：一个编号的类变量、一个奔跑速度的类变量和一个显示编号的类方法、一个现实奔跑速度的类方法
class Horse(object):
    Number = None
    Speed = "unknown"

    @classmethod
    def show_me_the_number(cls):
        print "the number is", cls.Number

# 田忌的马
# 甲种马
class Jia(Horse):
    Number = 0
    Speed = 90
# 乙种马
class Yi(Horse):
    Number = 1
    Speed = 80
# 丙种马
class Bing(Horse):
    Number = 2
    Speed = 70

# 齐威王的马
# 上等马
class Shang(Horse):
    Number = 0
    Speed = 95
# 中等马
class Zhong(Horse):
    Number = 1
    Speed = 85
# 下等马
class Xia(Horse):
    Number = 2
    Speed = 75

# 如果按套路对阵：田忌完败
# 田忌          齐威王         结果
# Jia(90)  vs.  Shang(95) --- 田忌败
# Yi(80)   vs.  Zhong(85) --- 田忌败
# Bing(70) vs.  Xia(75)   --- 田忌败
# 聪明的孙膑用计：田忌胜出
# 田忌          齐威王         结果
# Bing(70) vs.  Shang(95) --- 田忌败
# Jia(90)  vs.  Zhong(85) --- 田忌胜
# Yi(80)   vs.  Xia(75)   --- 田忌胜

# 马的编号容易泄密，只要“XXX.Number”就能拿到
print "Jia's Number is", Jia.Number
print "Yi's Number is", Yi.Number
print "Bing's Number is", Bing.Number

# 隐藏马的编号，就不逐个重新定义，以Horse为例
class Horse(object):
    __Number = 9527  # 假装没看到
    Speed = 100

    @classmethod
    def show_me_the_number(cls):
        print "the number is", cls.__Number

# print "Horse's __Number is", Horse.__Number
Horse.show_me_the_number()
