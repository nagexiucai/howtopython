#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2018/4/25 12:00
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : Repositories Synchronizer。

ROOT = "C:\\eclipse\\workspace"

GIT = ".git"
GITUPDATE = '"C:\\Program Files\\Git\\git-cmd.exe" git pull'

SVN = ".svn"
SVNUPDATE = '"C:\\Program Files\\TortoiseSVN\\bin\\svn.exe" update'

from os import chdir as CD
from os import listdir as DIR
from os import system as CALL
import os.path as PATH

def CALL(cmd):
    from subprocess import Popen, PIPE
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    msg = p.communicate()
    print(msg)

subdirs = DIR(ROOT)
print(subdirs)

print("=====START=====")
for project in subdirs:
    __ = PATH.join(ROOT, project)
    print(__)
    if PATH.isdir(__):
        CD(__)
        _ = DIR(__)
        print(_)
        if GIT in _:
            CALL(GITUPDATE)
        if SVN in _:
            CALL(SVNUPDATE)
        CD(ROOT)
print("=====END=====")
