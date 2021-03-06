#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/25 17:05
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 用马类定义马群。

# 当作从./simple.py中把Horse的定义抄写到此
from grasp.classes.horse.simple import Horse

# 先定义三匹马：的卢、赤兔、乌锥（张飞和项羽坐骑同名）

DiLu = Horse
ChiTu = Horse
WuZhui = Horse

# 这三匹马有着不同的名字、毛色、身高、体重、力量、速度、年级、食量……
print DiLu.Name, ChiTu.Name, WuZhui.Name

# 却是一样的名字
# 可以在定义每个马的时候，指明各自的名字
Horse.Name = "DiLu"
DiLu = Horse
print DiLu.Name

Horse.Name = "ChiTu"
ChiTu = Horse
print ChiTu.Name

Horse.Name = "WuZhui"
WuZhui = Horse
print WuZhui.Name

# 这样就有问题，再看看这三匹马的名字
print DiLu.Name, ChiTu.Name, WuZhui.Name
# 怎么全都是“WuZhui”，明明在定义时候，分别写的是“DiLu”、“ChiTu”、“WuZhui”么

# 因为所有的马名字，都用的Horse.Name，所有的马都是Horse的别名，此时，的卢、赤兔、乌锥是同一块肉
print id(DiLu), id(ChiTu), id(WuZhui)  # 显示每匹马的在内存中的地址的哈希值
