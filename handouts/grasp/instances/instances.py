#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/20 18:07
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 通过定义不同阶层的人类讲解封装、继承。
# 要特别说明的是，本例例是一次客串讲课时现场设计的。
# http://www.nagexiucai.com/topic.php?title=FourDaysInHuaiAn&md=inspiration-of-huaian
# 个站发布时有所修订，如特意把“CTO”修订为“SuperMan”以避免某些人的误会等。

class Person(object):

    '''
        人的基础类定义
    '''

    def __init__(self, name, _sex, __id):
        self.name = name # 姓名
        self._sex = _sex # 性别
        self._height, self._weight = None, None # 身高体重
        self.__id = __id # 身份证号

    def WhoAmI(self):
        print self.name

    def Insight(self):
        print self._sex, self._height, self._weight

    def WhoIsThat(self):
        print self.GetId()

    def Walk(self): # Q：人是怎么走的呢？
        print "one two one~" # A：一二一（给出一个包袱）

    def Eat(self): # Q：人是怎么吃的呢？
        print "bia-ji" # A：Bia-Ji

    def GetId(self):
        # TODO: 征得本人同意或具有某种特权
        return self.__id
    def SetId(self, __id):
        # TODO: 征得本人同意或具有某种特权
        self.__id = __id

    def GetSex(self):
        # TODO: 征得本人同意或具有某种特权
        return self._sex
    def SetId(self, _sex):
        # TODO: 征得本人同意或具有某种特权
        self._sex = _sex

    def GetHeight(self):
        return self._height
    def GetWeight(self):
        return self._weight

    def GetName(self):
        return self.name
    def SetName(self, name):
        # TODO: 征得本人同意或具有某种特权
        self.name = name

class ChairMan(Person):

    def Order(self): # Q：领导有什么特质？
        print "who is that guy" # A：发号施令（那个谁去把X干了）

    def Eat(self): # Q：主席怎么吃的呢？
        print "big dinner" # A：大餐

    def Walk(self):
        super(ChairMan, self).Walk() # 调用亲类方法
        print "left right left~"

class MaNong(Person):

    def Eat(self): # Q：码农怎么吃的呢？
        print "half-full" # A：半饱

class CTO(ChairMan, MaNong): # 既是领导又会写代码的就是吸啼噢

    def Fly(self): # Q：怎么飞？
        print "hula~" # A：呼啦-呼啦

person = Person("PingMin", "Any", 0)
person.Eat()
person.WhoAmI()

chairman = ChairMan("XiDada", "Secret", 20121115)
chairman.Eat()
chairman.Walk()
chairman.WhoAmI()

manong = MaNong("XiuCai", "PureMale", 9527)
manong.Eat()
manong.WhoAmI()

cto = CTO("XiMen", "Unknown", 20160905)
cto.Eat()
cto.Fly()
cto.WhoAmI()
