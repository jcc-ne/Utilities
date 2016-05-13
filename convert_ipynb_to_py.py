#!/usr/bin/env python

from nbformat import v3, v4
import sys
import optparse
import codecs
import os
import glob

usage = """usage: %prog <pyfile>
-----------------------------------------
this script will convert ipython notebook to python format with the mark:
# <codecell>
# <markdowncell>

"""

parser = optparse.OptionParser(usage=usage)
(opts, args) = parser.parse_args()
if len(args) != 1:
    print parser.get_usage()
    exit()

pyfile = args[0]
# with open(pyfile) as fpin:
#     text = fpin.read()

if os.path.splitext(pyfile)[1] != '.ipynb':
    print "please input ipynb file"
    exit()

f = codecs.open(pyfile, 'r', encoding='utf-8')
text = f.read()


nbook = v4.reads_json(text)
nbook = v4.downgrade(nbook)  # downgrade v4 to v3

pyform = v3.writes_py(nbook)
filename = pyfile.replace('.ipynb', ".py")

if glob.glob(filename):
    os.system('mv {} {}.bak'.format(filename, filename))

with open(filename, "w") as fpout:
    fpout.write(pyform.encode('utf-8'))
