#!/usr/bin/env python
#coding=utf-8

def show():
    print 'wow~'

class CLASS:
    x = None
    y = True
    z = show()
    def __init__(self):
        self.x = 'x'

c = CLASS()
cc = CLASS()
 
print c.x, c.y, c.z

#from class_attr__instance_attr import CLASS
#import like above, make instances like c/cc
#are all defined CLASS.z only once
