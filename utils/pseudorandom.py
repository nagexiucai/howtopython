#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/5/21 14:00
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 伪随机。

import random
import time

for i in xrange(7):
    print i, time.ctime()
    offset = 5 * 60 * (random.random() + 1)
    time.sleep(offset)
