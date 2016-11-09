#!/usr/bin/env python
#encoding=utf-8

import subprocess
import threading
import Queue

class CMD:
    def __init__(self, cmd):
        assert isinstance(cmd, basestring)
        self.cmd = cmd
    def __str__(self):
        return self.cmd
    __repr__ = __unicode__ = __str__

class IMT:
    def __init__(self, p, q):
        assert isinstance(p, subprocess.Popen)
        assert isinstance(q, Queue.Queue)
        self.p = p
        self.q = q
        self()
    def __call__(self):
        print 'perform %s (p=%s, q=%s)' % (self, self.p, self.q)

class Manager:
    def __init__(self, ti, to, te, p, qi, qoe):
        assert isinstance(ti, threading.Thread)
        assert isinstance(to, threading.Thread)
        assert isinstance(te, threading.Thread)
        assert isinstance(p, subprocess.Popen)
        assert isinstance(qi, Queue.Queue)
        assert isinstance(qoe, Queue.Queue)
        self.ti = ti
        self.to = to
        self.te = te
        self.p = p
        self.qi = qi
        self.qoe = qoe
        self()
    def __call__(self):
        print 'perform %s (ti=%s, to=%s, te=%s, p=%s, qi=%s, qoe=%s)' % (self, self.ti, self.to, self.te, self.p, self.qi, self.qoe)

def invoke(cmd, indication, monitor, treatment, manager):
    assert isinstance(cmd, CMD)
    assert issubclass(indication, IMT)
    assert issubclass(monitor, IMT)
    assert issubclass(treatment, IMT)
    assert issubclass(manager, Manager)
    p = subprocess.Popen(`cmd`, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    qi = Queue.Queue()
    qoe = Queue.Queue()
    ti = threading.Thread(target=indication, args=(p, qi))
    to = threading.Thread(target=monitor, args=(p, qoe))
    te = threading.Thread(target=treatment, args=(p, qoe))
    mngr = threading.Thread(target=manager, args=(ti, to, te, p, qi, qoe))
    mngr.setDaemon(True)
    mngr.start()
    mngr.join()
