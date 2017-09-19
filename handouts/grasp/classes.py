#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/19 19:06
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : 简述类的划分模式、大部分Python语法。

# 马类定义例程
# By Bob On 2017-09-13
class Horse(object):
    '''
    as base class for horse family.
    '''
    Species = "Horse"

    def run(self):
        self.stop = False
        Horse.clop()

    def stop(self):
        '''
        tell a horse to stop running.
        '''
        self.stop = True  # a mark for running or not

    @classmethod
    def clop(cls):
        while self.stop:
            print "clop~clop~"

    @classmethod
    def neigh(cls):
        print "nei~gh~~~"

    @classmethod
    def what_am_i(cls):
        print "I am a", Horse.Species

if __name__ == '__main__':
    Horse.neigh()
