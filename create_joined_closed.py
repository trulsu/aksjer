import pickle
import sys
import pandas as pd

def compile_data(tickerfile):
	with open(tickerfile, "rb") as f:
		tickers = pickle.load(f)

	main_df = pd.DataFrame()
	for count,ticker in enumerate(tickers):
		try:
			df = pd.read_csv('stockdata/{}.csv'.format(ticker))
			df.set_index('Date', inplace=True)
			df.rename(columns = {'Adj Close': ticker}, inplace=True)
			df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

			if main_df.empty:
				main_df = df
			else:
				main_df = main_df.join(df, how='outer')

			if count % 10 == 0:
				print(count)
		except:
			print("Error reading data for {} ignoring".format(ticker))

	print(main_df.head())
	main_df.to_csv('oslobors_joined_closed.csv')

if len(sys.argv) != 2:
	print("Usage: create_correlationplot.py tickerfile.pickle")
	print("Assumes you have downloaded stockdata in stockdata dir")
	exit()

tickerfile = sys.argv[1]
compile_data(tickerfile)