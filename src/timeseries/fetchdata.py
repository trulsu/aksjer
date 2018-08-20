import pandas as pd
import datetime as dt
import sys
import os
import sqlite3
from fetchdata_netfonds import get_tickerdata_from_netfonds

# We want a dataset that contains the following columns:
# ['date','ticker','open','close','high','low','close','volume']

# Get the last date from the datatable
def get_startdate(connection,tickerdb):
	start = dt.datetime(2010,1,1)
	if os.path.exists(tickerdb):
		try:
			cursor = connection.cursor()
			cursor.execute('select max(date) from data')
			rawdate = (cursor.fetchone()[0]).split(" ")[0]
			print('rawdate:{}'.format(rawdate))
			date = dt.datetime.strptime(rawdate, '%Y-%m-%d')
			date += dt.timedelta(days=1)
			start = date
		except:
			print("Exception in get_startdate: {}".format(sys.exc_info()[0]))
	return start

def get_enddate():
	today = dt.datetime.today()
	return dt.datetime(today.year, today.month, today.day)

def update_tickerdatadb(ticker,stop,datadir):
	try:
		tickerdb = "./{}/{}.sqlite".format(datadir, ticker)
		connection = sqlite3.connect(tickerdb, detect_types=sqlite3.PARSE_DECLTYPES)
		start = get_startdate(connection, tickerdb)
		end = get_enddate()
		df = get_tickerdata_from_netfonds(ticker, start, end)
		print(df.info)
		df.to_sql('data',con=connection,if_exists='append')
		connection.close()
	except:
		print("Error reading data for {}".format(ticker))
		print("Exception in update_tickerdatadb: {}".format(sys.exc_info()))
	connection.close()

def update_tickerdata(tickers, datadir):
	if not os.path.exists(datadir):
		os.makedirs(datadir)

	stop = get_enddate()
	for ticker in tickers:
		update_tickerdatadb(ticker,stop, datadir)
