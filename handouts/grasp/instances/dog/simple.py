#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/11/6 14:42
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 通过简单的狗类演示类的三大性质。

from grasp.classes.horse.simple import Horse

class HorseI(Horse):
    def __init__(self, number):
        self.number = number
        self.__age = "secret"
