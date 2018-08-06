

# Python way to read csv file from web
# import urllib2
# response = urllib2.urlopen('http://www.example.com/')
# html = response.read()

# https://www.netfonds.no/quotes/paperhistory.php?paper=OSEBX.OSE&csv_format=csv

import pandas as pd

def get_tickerdata_from_netfonds(ticker, start, end):
	uri = "https://www.netfonds.no/quotes/paperhistory.php?paper={}.OSE&csv_format=csv".format(ticker)
	df = pd.read_csv(uri,encoding='latin1')
	df.rename(columns = {'quote_date':'date','paper':'ticker'}, inplace = True)
	df = df [['date','ticker','open','close','high','low','close','volume']]
	return df
