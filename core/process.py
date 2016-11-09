#!/usr/bin/env python
#encoding=utf-8

import subprocess
import threading
import Queue

class IMT:
    def __init__(self, fd, pq):
        assert hasattr(fd, 'read') or hasattr(fd, 'write')
        assert isinstance(pq, Queue.PriorityQueue)
        self.fd = fd
        self.pq = pq

class Manager:
    def __init__(self, i, o, e, pq):
        assert isinstance(i, threading.Thread)
        assert isinstance(o, threading.Thread)
        assert isinstance(e, threading.Thread)
        assert isinstance(pq, Queue.PriorityQueue)
        self.i = i
        self.o = o
        self.e = e
        self.pq = pq

def invoke(cmd, indication, monitor, treatment, manager):
    assert isinstance(indication, IMT)
    assert isinstance(monitor, IMT)
    assert isinstance(treatment, IMT)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pq = Queue.PriorityQueue()
    stdin = threading.Thread(target=indication, p.stdin, pq)
    stdout = threading.Thread(target=monitor, p.stdout, pq)
    stderr = threading.Thread(target=treatment, p.stderr, pq)
    mngr = threading.Thread(target=manager, stdin, stdout, stderr, pq)
    mngr.setDaemon(True)
    mngr.start()
