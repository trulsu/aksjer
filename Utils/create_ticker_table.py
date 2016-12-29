#!/usr/bin/python

import sqlite3
import sys
from os import path

def create_ticker_entry(ticker, name, cursor):
	cursor.execute('''INSERT OR IGNORE INTO ticker(ticker,name) VALUES(?,?)''',
		(ticker, name))
	return

# Check command line parameters
if len(sys.argv) != 2:
	print 'Usage: download_stockdata list_of_companies'
	print '       Where the list of companies is expected to'
	print '       Be in the format of <ticker, name>'
	sys.exit()

#
company_file = sys.argv[1]
if not path.exists(company_file):
	print 'Cannot find company file: ', company_file
	sys.exit()

datadir = 'Data'

if not path.isdir(datadir):
	print 'Cannot find data directory: ', datadir
	sys.exit()

# Create or open a database file called mydb with a SQLite3 DB
db = sqlite3.connect(datadir + '/TickerList.sqlite3')
db.text_factory = str

# Create a table (data types: INTEGER, REAL, TEXT, BLOB)
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Ticker(ticker TEXT PRIMARY KEY,name TEXT)''')

# Read the file, inserting an entry for each company
with open(company_file, 'r') as tickerfile:
	for line in tickerfile:
		ticker, name = line.split(",")[:2]
		create_ticker_entry(ticker, name, cursor)
	cursor.execute()

print "Done"