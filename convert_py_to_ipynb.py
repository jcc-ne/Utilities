#!/usr/bin/env python

from nbformat import v3, v4
import sys
import optparse

usage = "usage: %prog <pyfile>"
parser = optparse.OptionParser(usage=usage)
(opts, args) = parser.parse_args()
if len(args) != 1:
    print parser.get_usage()
    exit()

pyfile = args[0]
with open(pyfile) as fpin:
    text = fpin.read()

nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

jsonform = v4.writes(nbook) + "\n"
with open(pyfile.replace('.py', ".ipynb"), "w") as fpout:
    fpout.write(jsonform)
