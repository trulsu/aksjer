#!/usr/bin/python

import sys
sys.path.insert(0, './src/tickers/')

import pandas as pd
import os
from fetchdata import update_tickerdata

if not os.path.isfile('./Data/selskapsliste_formatert.csv'):
	print("Missing file Data/selskapsliste_formatert.csv")
	print("Run the initialize.py script first to create this")
	exit

selskaper = pd.read_csv('./Data/selskapsliste_formatert.csv',index_col=0)
update_tickerdata(selskaper.Tickers.tolist(), './Data/')