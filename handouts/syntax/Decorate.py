#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/20 16:58
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 演示Python中的装饰器。


def wrapper(inner, *args, **kwargs):
    print "wrapper", args, kwargs
    print inner
    return inner(*args, **kwargs)


def coverage(indoor, *args, **kwargs):
    print "indoor", args, kwargs
    print indoor
    return indoor(*args, **kwargs)


def test(*args, **kwargs):
    print args, kwargs


@wrapper
def test_(*args, **kwargs):
    print args, kwargs
    return lambda x: test("lambda under test_", x)


@coverage
@wrapper
def test__(*args, **kwargs):
    print args, kwargs
    return lambda: lambda x: test("lambda under test__", x)


test("bare")
test_("egg")
test__("onion")

def a(*args, **kwargs):
    def b(f):
        return f(*args, **kwargs)
    return b


@a('xy', x=0, y='0')
def c(*args, **kwargs):
    print "c", args, kwargs
    return lambda *args, **kwargs: test(*args, **kwargs)

c("ij", i=None, j="None")