#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/22 10:59
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 类的继承。

# TODO: 不能简单的将“仅有前缀下划线”的作用和Java/C++的“public”、“protected”、“private”对应理解

from syntax.PrivateAttributeFullName import V, pprint

# 子类公开、父类公开
# 子类可以访问父类非私有属性
class VV(V):
    PhoneCode = "PC"
    _PhoneCode = "_PC"
    __PhoneCode = "__PC"
    @classmethod
    def show_phone_code(cls):
        print cls.PhoneCode
    @classmethod
    def _show_phone_code(cls):
        print cls._PhoneCode
    @classmethod
    def __show_phone_code(cls):
        print cls.__PhoneCode
    def __init__(self):
        V.__init__(self)
        self.__address = "secret"
        self._address = "protected"
        self.address = "public"
    def show_address(self):
        print self.address
    def _show_address(self):
        print self._address
    def __show_address(self):
        print self.__address
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name      # O
        print cls._Name     # O
        # print cls.__Name    # X
        cls.face()          # O
        cls._face()         # O
        # cls.__face()        # X
    def what_can_i_see_now_instance(self):
        print self.age      # O
        print self._age     # O
        # print self.__age    # X
        self.how_old()      # O
        self._how_old()     # O
        # self.__how_old()    # X

# 子类保护、父类公开
# 子类可以访问父类非私有的属性
class _VV(V):
    PhoneCode = "PC"
    _PhoneCode = "_PC"
    __PhoneCode = "__PC"
    @classmethod
    def show_phone_code(cls):
        print cls.PhoneCode
    @classmethod
    def _show_phone_code(cls):
        print cls._PhoneCode
    @classmethod
    def __show_phone_code(cls):
        print cls.__PhoneCode
    def __init__(self):
        V.__init__(self)
        self.__address = "secret"
        self._address = "protected"
        self.address = "public"
    def show_address(self):
        print self.address
    def _show_address(self):
        print self._address
    def __show_address(self):
        print self.__address
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name      # O
        print cls._Name     # O
        # print cls.__Name    # X
        cls.face()           # O
        cls._face()          # O
        # cls.__face()        # X
    def what_can_i_see_now_instance(self):
        print self.age      # O
        print self._age     # O
        # print self.__age    # X
        self.how_old()       # O
        self._how_old()      # O
        # self.__how_old()    # X

# 子类私有、父类公开
# 子类可以访问父类非私有的属性
class __VV(V):
    PhoneCode = "PC"
    _PhoneCode = "_PC"
    __PhoneCode = "__PC"
    @classmethod
    def show_phone_code(cls):
        print cls.PhoneCode
    @classmethod
    def _show_phone_code(cls):
        print cls._PhoneCode
    @classmethod
    def __show_phone_code(cls):
        print cls.__PhoneCode
    def __init__(self):
        V.__init__(self)
        self.__address = "secret"
        self._address = "protected"
        self.address = "public"
    def show_address(self):
        print self.address
    def _show_address(self):
        print self._address
    def __show_address(self):
        print self.__address
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name      # O
        print cls._Name     # O
        # print cls.__Name    # X
        cls.face()           # O
        cls._face()          # O
        # cls.__face()        # X
    def what_can_i_see_now_instance(self):
        print self.age      # O
        print self._age     # O
        # print self.__age    # X
        self.how_old()       # O
        self._how_old()      # O
        # self.__how_old()    # X

# 验证VV
# pprint(dir(VV))
# VV.what_can_i_see_now_class()
# vv = VV()
# pprint(dir(vv))
# vv.what_can_i_see_now_instance()

# 验证_VV
# pprint(dir(_VV))
# _VV.what_can_i_see_now_class()
# _vv = _VV()
# pprint(dir(_vv))
# _vv.what_can_i_see_now_instance()

# 验证__VV
# pprint(dir(__VV))
# __VV.what_can_i_see_now_class()
# __vv = __VV()
# pprint(dir(__vv))
# __vv.what_can_i_see_now_instance()

# 子类公开、父类保护
# 子类可以访问父类非私有的属性
class VVV(_VV):
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name
        print cls._Name
        # print cls.__Name  # X
        print cls.PhoneCode
        print cls._PhoneCode
        # print cls.__PhoneCode # X
        cls.show_phone_code()
        cls._show_phone_code()
        # cls.__show_phone_code()  # X
    def what_can_i_see_now_instance(self):
        print self.age
        print self._age
        # print self.__age  # X
        print self.address
        print self._address
        # print self.__address  # X
        self.show_address()
        self._show_address()
        # self.__show_address()  # X

# 验证VVV
# pprint(dir(VVV))
# VVV.what_can_i_see_now_class()
# vvv = VVV()
# pprint(dir(vvv))
# vvv.what_can_i_see_now_instance()

# 子类公开、父类私有
# 子类可以访问父类非私有属性
class VVVX(__VV):
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name
        print cls._Name
        # print cls.__Name  # X
        print cls.PhoneCode
        print cls._PhoneCode
        # print cls.__PhoneCode # X
        cls.show_phone_code()
        cls._show_phone_code()
        # cls.__show_phone_code()  # X
    def what_can_i_see_now_instance(self):
        print self.age
        print self._age
        # print self.__age  # X
        print self.address
        print self._address
        # print self.__address  # X
        self.show_address()
        self._show_address()
        # self.__show_address()  # X

# 验证VVVX
# pprint(dir(VVVX))
# VVVX.what_can_i_see_now_class()
# vvvx = VVVX()
# pprint(dir(vvvx))
# vvvx.what_can_i_see_now_instance()

# 子类保护、父类保护
# 子类保护、父类私有

# 子类私有、父类保护
# 子类私有、父类私有

# 子类私有、父类私有、在子类私有方法中调用父类属性
class __VVVX(__VV):
    @classmethod
    def what_can_i_see_now_class(cls):
        print cls.Name
        print cls._Name
        # print cls.__Name  # X
        print cls.PhoneCode
        print cls._PhoneCode
        # print cls.__PhoneCode # X
        cls.show_phone_code()
        cls._show_phone_code()
        # cls.__show_phone_code()  # X
    @classmethod
    def _what_can_i_see_now_class(cls):
        print cls.Name
        print cls._Name
        # print cls.__Name  # X
        print cls.PhoneCode
        print cls._PhoneCode
        # print cls.__PhoneCode # X
        cls.show_phone_code()
        cls._show_phone_code()
        # cls.__show_phone_code()  # X
        cls.__what_can_i_see_now_class()
    @classmethod
    def __what_can_i_see_now_class(cls):
        print cls.Name
        print cls._Name
        # print cls.__Name  # X
        print cls.PhoneCode
        print cls._PhoneCode
        # print cls.__PhoneCode # X
        cls.show_phone_code()
        cls._show_phone_code()
        # cls.__show_phone_code()  # X
    def what_can_i_see_now_instance(self):
        print self.age
        print self._age
        # print self.__age  # X
        print self.address
        print self._address
        # print self.__address  # X
        self.show_address()
        self._show_address()
        # self.__show_address()  # X
        self.__what_can_i_see_now_instance()
    def _what_can_i_see_now_instance(self):
        print self.age
        print self._age
        # print self.__age  # X
        print self.address
        print self._address
        # print self.__address  # X
        self.show_address()
        self._show_address()
        # self.__show_address()  # X
        self.__what_can_i_see_now_instance()
    def __what_can_i_see_now_instance(self):
        print self.age
        print self._age
        # print self.__age  # X
        print self.address
        print self._address
        # print self.__address  # X
        self.show_address()
        self._show_address()
        # self.__show_address()  # X

__VVVX.what_can_i_see_now_class()
__VVVX._what_can_i_see_now_class()
__vvvx = __VVVX()
__vvvx.what_can_i_see_now_instance()
__vvvx._what_can_i_see_now_instance()
