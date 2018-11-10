#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/31 13:09
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 那些多余的ELSE分支。

# for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]

for x in range(9):
    print x
else:
    print "over for"

n = 99
while n:
    print n
    n -= 1
else:
    print "over while"
