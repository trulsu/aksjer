#!/usr/bin/python

import pickle
import pandas as pd
import os
import sqlite3
import sys

def read_tickerfile(tickerfile):
	with open(tickerfile, "rb") as f:
		tickers = pickle.load(f)
	return tickers

def convert_csv_sqlite(tickers):
	 if not os.path.exists('stockdata'):
	 	print('Cannot find the stockdata directory')
	 	return

	 for ticker in tickers:
	 	print(ticker)
	 	tickercsv = 'stockdata/{}.csv'.format(ticker)
	 	if os.path.exists(tickercsv):
	 		tickerdb = 'stockdata/{}.sqlite'.format(ticker)
	 		
		 	try:
		 		df = pd.read_csv(tickercsv, index_col = 0)
		 		connection = sqlite3.connect(tickerdb, detect_types=sqlite3.PARSE_DECLTYPES)
	 			df.to_sql(name='data',con=connection,if_exists='append')
	 			connection.close()
	 		except IntegrityError:
	 			pass
	 		except:
	 			print("Error reading data for {}".format(ticker))
	 	else:
	 		print('\tCannot find csv file for {}'.format(ticker))

if len(sys.argv) != 2:
	print("Usage: import_tickerdata.py tickerfile.pickle")
	exit()

tickerfile = sys.argv[1]
tickers = read_tickerfile(tickerfile)
convert_csv_sqlite(tickers)
