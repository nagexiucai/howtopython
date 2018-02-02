#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/2/2 10:33
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary :

import threading
import time

def bored(x):
    print "start", x
    N = 100000000
    for i in xrange(N):
        if 0 == i%1000000:
            print x, i
    print "end", x

def mice():
    print "start mice"
    time.sleep(9.527)
    print "end mice"

def main():
    threads = []
    M = 9
    for i in range(M):
        # if i == M/2:
        #     t = threading.Thread(target=mice, name="Mice")
        # else:
        #     t = threading.Thread(target=bored, name="Bored %d" % i, args=(i,))
        t = threading.Thread(target=bored, name="Bored %d" % i, args=(i,))
        threads.append(t)
    t = threading.Thread(target=mice, name="Mice")
    threads.insert(0, t)
    for _ in threads:
        _.start()
        # _.join(0)

if __name__ == "__main__":
    now = time.time()
    main()
    print time.time() - now
