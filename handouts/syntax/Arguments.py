#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/16 04:55
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 演示Python函数参数定义。

def function(argumentA, argumentB, name="name", *arguments, **kwArguments):
    print argumentA, argumentB
    print name
    print arguments
    print kwArguments
    return "We can return more than one in one or each of them here"

function("A", "B", "C", "D", "bob", age=None, sex=None)
