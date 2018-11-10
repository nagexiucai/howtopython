#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/7/28 13:22
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary :　专题。

class HowAmI(object): # TODO: 按某种规则各个分段哈希和整体哈希一致。
    '''
    though dict[keya,keyb,...]=value.
    '''
    __attributes__ = set()
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__attributes__.add(k)
            setattr(self, k, v)
        self.__attributes__ = tuple(sorted(self.__attributes__))
    def __eq__(self, gd):
        for attribute in self.__attributes__:
            if not getattr(self, attribute) == getattr(gd, attribute):
                return False
        return True
    def __cmp__(self, gd):
        for attribute in self.__attributes__:
            if not cmp(getattr(self, attribute), getattr(gd, attribute)):
                return False
        return True
    def __hash__(self):
        return hash(u" ".join([unicode(getattr(self, _)) for _ in self.__attributes__]))
    def __unicode__(self):
        return " ".join([u"%s=%s" % (k, getattr(self, k)) for k in self.__attributes__])
    __str__ = __unicode__
    def __repr__(self):
        return "%d %s" % (id(self), self)

x = HowAmI(x=0, y=0, z=0)
y = HowAmI(x=0, y=0, z=0)
z = HowAmI(x=0, y=0, z=1)

s = set()
d = {}

s.add(x)
s.add(y)
s.add(z)

d[x] = 1314
d[y] = 9527
d[z] = 1005

print s
print d

class FunnySet(set):
    def __contains__(self, item):pass
