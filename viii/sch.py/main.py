#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/11/10 12:46
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 基于Python3构建中文编程语言。

# LEVEL-kindergarten: 禁用字符串替换解析。

# from keyword import kwlist
# print(kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

KWMAP = {
    'False': u"假",
    'None': u"屁",
    'True': u"真",
    'and': u"且",
    'or': u"或",
    'as': u"作",
    'assert': u'必有',
    'break': u"中止",
    'class': u"类",
    'continue': u"继续",
    'def': u"过程",
    'elif': u"或是",
    'else': u"否则",
    'except': u"异常",
    'finally': u"最后",
    'for': u'遍历',
    'from': u"自",
    'global': u"全局",
    'if': u"若是",
    'import': u"导入",
    'in': u"在于",
    'is': u"即",
    'lambda': u"函数",
    'nonlocal': u"非本地",
    'not': u"否",
    'pass': u"还没想好",
    'raise': u"起义",
    'return': u"返回",
    'try': u"尝试",
    'while': u"循环",
    'with': u"伴随",
    'yield': u"抛出"
}

KWMAPOPPO = {}
for k, v in KWMAP.items():
    KWMAPOPPO[v] = k

# TODO: @ async wait

TEST = u'''#!/usr/bin/env python
# -*- encoding: utf-8 -*-

自 os 导入 getcwd
print(getcwd())

# 测试

"""
test
"""

类 人:
  过程 __init__(吾, 姓名, 年龄, 电话号码):
    吾.姓名 = 姓名
    吾._年龄 = 年龄
    吾.__电话号码 = 电话号码
  过程 __str__(吾):
    返回 u"姓名：%s，年龄：%s，电话号码：%s。" % (吾.姓名, 吾._年龄, 吾.__电话号码)

用户 = 人(u"秀才", 28, u"秘密")
print(用户)
'''

def parse(code):
    codecopy = code
    for k, v in KWMAPOPPO.items():
        codecopy = codecopy.replace(k, v)
    return codecopy

PY = parse(TEST)
# print(PY)

exec(PY)
