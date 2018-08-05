import sys
sys.path.insert(0, '../src/timeseries/')

import pandas as pd
from fetchdata_netfonds import get_tickerdata_from_netfonds

if len(sys.argv) != 2:
	print("Usage: fetchtickerdata TICKER")
	print(str(sys.argv))
	exit

ticker = sys.argv[1]

df = get_tickerdata_from_netfonds(ticker, 1, 1)
print(df.head())