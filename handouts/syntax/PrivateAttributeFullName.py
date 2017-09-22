#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/22 10:38
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 私有属性的全名起底。

from pprint import pprint

class V(object):  # 受《V for Vendetta》启发
    Name = "V"
    _Name = "_V"
    __Name = "__V"
    @classmethod
    def __face(cls):
        print "In view, a humble vaudevillian veteran cast vicariously as both victim and villain by the vicissitudes of fate."
    @classmethod
    def _face(cls):
        print "This visage, no mere veneer of vanity is a vestige of the vox populi, now vacant, vanished."
    @classmethod
    def face(cls):
        print "However, this valorous visitation of a bygone vexation stands vivified and has vowed to vanquish these venal and virulent vermin vanguarding vice and vouchsafing the violently vicious and voracious violation of volition."
    def __init__(self):
        self.__age = "private"
        self._age = "protected"
        self.age = "public"
    def __how_old(self):
        print self.__age
    def _how_old(self):
        print self._age
    def how_old(self):
        print self.age

if __name__ == "__main__":
    v = V()
    pprint(dir(V))
    pprint(dir(v))
