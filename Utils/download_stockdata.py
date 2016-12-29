#!/usr/bin/python

import sys
from os import path

def foo(arg):
	print arg

if len(sys.argv) != 2:
	print 'Usage: download_stockdata list_of_companies'
	print '       Where the list of companies is expected to'
	print '       Be in the format of <ticker, name>'
	sys.exit()

basedir = sys.argv[1]

if not path.isdir(basedir):
	print 'Cannot find basedir: ', basedir
	sys.exit()

datadir = basedir + '/Data'

if not path.isdir(datadir):
	print 'Cannot find data directory: ', datadir
	sys.exit()

