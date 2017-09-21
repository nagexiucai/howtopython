#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:40
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 验证能够访问隐藏的马类属性的办法。

# 拍脑袋想出的验证办法
# 一、在Horse的类方法show_me_the_number中也用“Horse.__Number”取马的编号
# 二、在别的地方也用“cls.__Number”取马的编号
class Horse(object):
    __Number = 9527  # 假装没看到
    Speed = 100

    @classmethod
    def show_me_the_number(cls):
        print "the number is", Horse.__Number

# print "Horse's __Number is", cls.__Number  # 二
Horse.show_me_the_number()  # 一
