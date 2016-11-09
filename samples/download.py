#!/usr/bin/env python
#coding=utf-8

from core.process import CMD, IMT, Manager, invoke

class Indication(IMT):
    def __call__(self):
        while True:
            data = self.q.get()
            if data:
                print 'indication data:', data
                self.p.stdin.write(data)
class Monitor(IMT):
    def __call__(self):
        while True:
            data = self.p.stdout.read()
            if data:
                print 'monitor data:', data
                self.q.put(data)
class Treatment(IMT):
    def __call__(self):
        while True:
            data = self.p.stderr.read()
            if data:
                print 'treatment data:', data
                self.q.put(data)

class Download(Manager):
    def __call__(self):
        self.ti.start()
        self.to.start()
        self.te.start()
        self.p.wait()
        print 'manager:', self.qoe.get()

def download(cmd):
    invoke(CMD(cmd), Indication, Monitor, Treatment, Download)

if __name__ == '__main__':
    download('scp root@192.168.10.190:/home/bob/sources .')
