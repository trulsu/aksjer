import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import sys
import os
import sqlite3

# Get the last date from the datatable
def get_startdate(connection):
	cursor = connection.cursor()
	cursor.execute('select max(date) from data')
	rawdate = (cursor.fetchone()[0]).split(" ")[0]
	print('rawdate:{}'.format(rawdate))
	date = dt.datetime.strptime(rawdate, '%Y-%m-%d')
	date += dt.timedelta(days=1)
	return date

def get_data_from_yahoo(tickers):
	 if not os.path.exists('stockdata'):
	 	os.makedirs('stockdata')

	 start = dt.datetime(2010,1,1)
	 today = dt.datetime.today()
	 end = dt.datetime(today.year, today.month, today.day)

	 for ticker in tickers:
	 	print(ticker)
	 	tickerdb = 'stockdata/{}.sqlite'.format(ticker)
	 	tickerdb_exists = os.path.exists(tickerdb)
	 	connection = sqlite3.connect(tickerdb, detect_types=sqlite3.PARSE_DECLTYPES)

	 	if tickerdb_exists:
	 		try:
	 			start = get_startdate(connection)
	 		except:
	 			pass
 		try:
 			df = web.DataReader(ticker, 'yahoo', start ,end)
 			df.to_sql(name='data',con=connection,if_exists='append')
 		except:
 			print("Error reading data for {}".format(ticker))

 		connection.close()

def import_tickerdata(tickers):
	get_data_from_yahoo(tickers)
	
