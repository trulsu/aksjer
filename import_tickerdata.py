#!/usr/bin/python

import pickle
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import sys
import os

def read_tickerfile(tickerfile):
	with open(tickerfile, "rb") as f:
		tickers = pickle.load(f)
	return tickers

def get_data_from_yahoo(tickers):
	 if not os.path.exists('stockdata'):
	 	os.makedirs('stockdata')

	 start = dt.datetime(2000,1,1)
	 end = dt.datetime(2016,12,31)

	 for ticker in tickers:
	 	print(ticker)
	 	if not os.path.exists('stockdata/{}.csv'.format(ticker)):
	 		try:
	 			df = web.DataReader(ticker, 'yahoo', start ,end)
	 			df.to_csv('stockdata/{}.csv'.format(ticker))
	 		except:
	 			print("Error reading data for {}".format(ticker))
	 	else:
	 		print('Already have {}'.format(ticker))

if len(sys.argv) != 2:
	print("Usage: import_tickerdata.py tickerfile.pickle")
	exit()

tickerfile = sys.argv[1]
tickers = read_tickerfile(tickerfile)
get_data_from_yahoo(tickers)
