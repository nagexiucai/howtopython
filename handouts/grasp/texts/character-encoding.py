#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/26 16:46
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary :　字符编码。

a = "hi, nagexiucai.com"
b = "没错，就是那个秀才"
c = "没错，就是那个秀才".decode("utf-8")
d = u"没错，就是那个秀才"
e = "没错，就是那个秀才".decode("utf-8").encode("gbk")

print a, b, c, d, e
