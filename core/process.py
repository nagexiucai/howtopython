#!/usr/bin/env python
#encoding=utf-8

import subprocess
import threading
import Queue

CONFIG = {
    'stdin':subprocess.PIPE,
    'stdout':subprocess.PIPE,
    'stderr':subprocess.PIPE
    }

class Worker:
    def __init__(self, p, q):
        assert isinstance(p, subprocess.Popen)
        assert isinstance(q, Queue.Queue)
        self.p = p
        self.q = q
    def __call__(self):
        self.do()
    def do(self):
        print 'do %s (p=%s, q=%s)' % (self, self.p, self.q)
    def get(self):
        try:
            return self.q.get(False)
        except Queue.Empty:
            return False
    def put(self, data):
        self.q.put(data)
    def readout(self):
        data = self.p.stdout.read()
        if data: self.put(data)
    def readerr(self):
        data = self.p.stderr.read()
        if data: self.put(data)
    def write(self):
        data = self.get()
        if data:
            self.p.stdin.write(data)
            self.p.stdin.flush()

class Manager(threading.Thread):
    def __init__(self, cmd, i, o, e):
        super(Manager, self).__init__()
        self.qi = Queue.Queue()
        self.qoe = Queue.Queue()
        self.p = subprocess.Popen(cmd, shell=True, **CONFIG)
        self.i = threading.Thread(target=i(self.p, self.qi))
        self.o = threading.Thread(target=o(self.p, self.qoe))
        self.e = threading.Thread(target=e(self.p, self.qoe))
        self.setDaemon(True)
        self.i.start()
        self.o.start()
        self.e.start()
    def run(self):
        print 'run %s' % self

if __name__ == '__main__':
    Manager('ping localhost', Worker, Worker, Worker).start()
#     sp =subprocess.Popen('ping localhost', **CONFIG)
#     _, __ = sp.communicate()
#     print _, __
