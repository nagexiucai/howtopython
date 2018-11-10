#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os import getcwd
print(getcwd())

# 测试

"""
test
"""

class 人:
  def __init__(吾, 姓名, 年龄, 电话号码):
    吾.姓名 = 姓名
    吾._年龄 = 年龄
    吾.__电话号码 = 电话号码
  def __str__(吾):
    return u"姓名：%s，年龄：%s，电话号码：%s。" % (吾.姓名, 吾._年龄, 吾.__电话号码)

用户 = 人(u"秀才", 28, u"秘密")
print(用户)
