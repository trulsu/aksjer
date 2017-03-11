#!/usr/bin/python

import pickle
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import sys
import os
import sqlite3

def read_tickerfile(tickerfile):
	with open(tickerfile, "rb") as f:
		tickers = pickle.load(f)
	return tickers

# Get the last date from the datatable
def get_startdate(connection):
	connection.execute('select max(date) as "date [timestamp]" from data')
	return connection.first()

def get_data_from_yahoo(tickers):
	 if not os.path.exists('stockdata'):
	 	os.makedirs('stockdata')

	 start = dt.datetime(2000,1,1)
	 end = dt.today()

	 for ticker in tickers:
	 	print(ticker)
	 	tickerdb = 'stockdata/{}.sqlite'.format(ticker)
	 	tickerdb_exists = os.path.exists(tickerdb)
	 	connection = sqlite3.connect(tickerdb, detect_types=sqlite3.PARSE_DECLTYPES)

	 	if tickerdb_exists:
	 		start = get_startdate(connection)
	 		print('\tticker exists, starting at {}'.format(start))
 		try:
 			df = web.DataReader(ticker, 'yahoo', start ,end)
 			df.to_sql('data', connection)
 		except:
 			print("Error reading data for {}".format(ticker))

 		connection.close()

if len(sys.argv) != 2:
	print("Usage: import_tickerdata.py tickerfile.pickle")
	exit()

tickerfile = sys.argv[1]
tickers = read_tickerfile(tickerfile)
get_data_from_yahoo(tickers)
