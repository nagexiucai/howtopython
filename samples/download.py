#!/usr/bin/env python
#coding=utf-8

from core.process import Worker, Manager

class Indication(Worker):
    def do(self):
        while True:
            self.write()
class Monitor(Worker):
    def do(self):
        while True:
            self.readout()
class Treatment(Worker):
    def do(self):
        while True:
            self.readerr()

class Download(Manager):
    def run(self):
        #self.p.wait()
        while True:
            print self.qoe.get()

if __name__ == '__main__':
    cmd = 'ping -n 29 localhost'
    Download(cmd, Indication, Monitor, Treatment).start()
