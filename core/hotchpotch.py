#!/usr/bin/env python
#coding=utf-8

import Queue
import threading

class DNA(object):
    'DeoxyriboNecleic Acid'
    def __init__(self, *args, **kwargs):
        'True Good Beauty'
        self.__backend = 'deity'
    def born(self):
        pass
    def study(self):
        pass
    def labour(self):
        pass
    def restore(self):
        pass
    def marry(self):
        pass
    def replicate(self):
        pass
    def breed(self):
        pass
    def die(self):
        pass

class TDM(DNA):
    'Time Division Multiplex'
    def __init__(self, *args, **kwargs):
        super(TDM, self).__init__(*args, **kwargs)
    def born(self, moil, *args):
        self.engine = threading.Thread(target=moil, args=args)
    def labour(self):
        self.engine.start()

class CDM(DNA):
    'CPU Division Multiplex'

class MQD(DNA):
    'Message Queue Driven'
    def __init__(self, *args, **kwargs):
        super(MQD, self).__init__(*args, **kwargs)
    def born(self, limit):
        self.engine = Queue.PriorityQueue(maxsize=limit)

class FLP(TDM, MQD):
    'Flow Line Production'
    def __init__(self, *args, **kwargs):
        super(FLP, self).__init__(*args, **kwargs)
