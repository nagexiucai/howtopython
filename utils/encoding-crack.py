#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/8/16 19:11
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 字符编码爆破。

s = ur'''CONTEXT:  鎷疯礉 PIS_BASEINFO, 琛?392454: "836001	\N	1	\N		鍏ㄩ儴琛屾斂鍖哄垝鈥︹?	2015-11-24 00:00:00	01010312	\N	\N	1	1	2015-11-24 16:42:54	05600038..."'''
print s.encode('gbk')

ss = u'''琛'''
_ = '''行'''
print [ss], [ss.encode('gbk')]
print [_]

sss = u'''︹'''
_ = '''…'''
print [sss], [sss.encode('utf8')]
print [_]

x = ur'''ERROR:  鍒?FILEDS35"缂哄皯鏁版嵁'''
print x.encode('gbk')

xx = u'''鍒'''
_ = '''字'''
print [xx], [xx.encode('gbk')]
print [_]

y = ur'''ERROR:  鍏崇郴"PIS_BASEINFO"宸茬粡瀛樺湪'''
print y.encode('gbk')

z = ur'''WARNING:  鐢ㄦ埛宸茬粡鏄〃"PIS_BASEINFO"鐨勬墍鏈夎?'''
z = ur'''WARNING:    ㄦ埛宸茬粡〃"PIS_BASEINFO"鐨勬墍鏈夎?'''
z = ur'''WARNING:    ㄦ埛宸茬粡〃"PIS_BASEINFO"鐨勬墍鏈夎'''
print [z]
print z.encode('gbk')
