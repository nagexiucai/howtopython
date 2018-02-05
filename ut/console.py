#!/usr/bin/env python
#coding=utf-8

import optparse

parser = optparse.OptionParser()

parser.add_option("--who", "-w", dest="xiucai")
parser.set_default("xiucai", "nagexiucai")

parser.add_option("--age", "-a", dest="age")
parser.add_option("--sec", "-s", dest="sex")

parser.add_option("--verbose", "-v", dest="verbose", action="store_true")
parser.set_default("verbose", False)

opts, args = parser.parse_args(args=["-a 17", "-s female"])
print opts, args

opts, args = parser.parse_args(args=["-a 17", "-s female", "-v"])
print opts, args
