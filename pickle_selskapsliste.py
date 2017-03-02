#!/usr/bin/python

import sys
import pickle

if len(sys.argv) != 3:
	print("Usage: formater_selskapsliste <inputfile> <outputfile>")
	print(str(sys.argv))
	exit

inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile, 'r') as file:
	lines = file.read().split('\n')

tickers = [e + '.OL' for e in lines if e.upper() == e and e.strip() and ' ' not in e]
tickers = sorted(list(set(tickers)))

with open(outputfile, "wb") as f:
	pickle.dump(tickers,f)

# Test
with open(outputfile,"rb") as f:
	result = pickle.load(f)
	print("\n".join(result))