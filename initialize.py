#!/usr/bin/python

import sys
sys.path.insert(0, './src/tickers/')

import pandas as pd
import os
from formater_selskapsliste import formater_selskapsliste

if not os.path.isfile('./Data/Selskapsliste_uformatert.txt'):
	print("Missing file Data/Selskapsliste_uformatert.txt")
	print("See: Data/README.TXT for instructions")
	exit

formater_selskapsliste('./Data/Selskapsliste_uformatert.txt','./Data/selskapsliste_formatert.csv')
