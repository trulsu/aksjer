#!/usr/bin/python3

import sys
import pandas as pd

def create_pandas(ticker_list, name_list, exchange_list):
	ticker = pd.Series(ticker_list)
	name = pd.Series(name_list)
	exchange = pd.Series(exchange_list)
	colnames = ['Ticker','Name','Exchange']
	df = pd.concat([ticker, name, exchange], axis=1)
	df.columns = colnames
	df = df[df['Exchange'] == 'Oslo Børs']
	return df[['Ticker','Name']]

def remove_lines(lines):
	lines = [x for x in lines if not x == 'Primærnotert']
	prefixes = ('JA/','JA ','Nei/','Ja/')
	lines = [x for x in lines if not x.startswith(prefixes)]
	return lines

def formater_selskapsliste(inputfile,outputfile):
	with open(inputfile, 'r') as file:
		lines = file.read().split('\n')
	lines = remove_lines(lines)
	tickers   = lines[0::4]
	names     = lines[1::4]
	exchanges = lines[2::4]
	df = create_pandas(tickers, names, exchanges)
	df.to_csv(outputfile)

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print("Usage: formater_selskapsliste <inputfile> <outputfile>")
		print(str(sys.argv))
		exit

	inputfile = sys.argv[1]
	outputfile = sys.argv[2]

	formater_selskapsliste(inputfile,outputfile)
