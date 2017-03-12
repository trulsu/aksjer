#!/usr/bin/python

"""
Analyse updates the tickerdata and runs our basic analysis.
It then writes the resulting analysis to the result file,
which we can then use further.

Plan for now:
- Take all the scripts and create a utils module for them,
  which will then be used from this script.

- Create a settings file which will be used by this script

In the end I want:
- analyze: updates and runs basic analysis on ticker data
- plot: takes a ticker and plot(s) to output

"""

import json
import pickle
from pprint import pprint # Pretty print
from ticker import tickerdata as td

# Read the settings.json file to get our settings
def read_settings():
	try:
		with open('settings.json') as settings_file:
			settings = json.load(settings_file)
	except:
		print('Could not read settings.json')
	return settings

def read_tickerfile(tickerfile):
	try:
		with open(tickerfile, "rb") as f:
			tickers = pickle.load(f)
	except:
		print('could not read tickerfile: "{}"'.format(tickerfile))
		exit()
	return tickers

settings = read_settings()
tickerfile = settings["tickerfile"]
tickers = read_tickerfile(tickerfile)
td.import_tickerdata(tickers)