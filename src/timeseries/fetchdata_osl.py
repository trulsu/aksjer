# https://www.oslobors.no/ob/servlets/excel?
# type=history&columns=DATE%2C+CLOSE_CA%2C+BID_CA%2C+ASK_CA%2C+HIGH_CA%2C+LOW_CA%2C
# +TURNOVER_TOTAL%2C+VOLUME_TOTAL_CA%2C+TRADES_COUNT%2C+TRADES_COUNT_TOTAL%2C+VWAP_CA&
# format[DATE]=ddd.mm.YY&format[CLOSE_CA]=%23%2C%23%230.00%23%23%23
# &format[BID_CA]=%23%2C%23%230.00%23%23&format[ASK_CA]=%23%2C%23%230.00%23%23
# &format[HIGH_CA]=%23%2C%23%230.00%23%23%23&format[LOW_CA]=%23%2C%23%230.00%23%23%23
# &format[TURNOVER_TOTAL]=%23%2C%23%230&format[VOLUME_TOTAL_CA]=%23%2C%23%230
# &format[TRADES_COUNT]=%23%2C%23%230&format[TRADES_COUNT_TOTAL]=%23%2C%23%230
# &format[VWAP_CA]=%23%2C%23%230.00%23%23%23&header[DATE]=AEGA&header[CLOSE_CA]=Siste
# &header[BID_CA]=Kj%C3%B8per&header[ASK_CA]=Selger&header[HIGH_CA]=H%C3%B8y
# &header[LOW_CA]=Lav&header[TURNOVER_TOTAL]=Totalt%20omsatt%20%28NOK%29
# &header[VOLUME_TOTAL_CA]=Totalt%20antall%20aksjer%20omsatt
# &header[TRADES_COUNT]=Antall%20off.%20handler
# &header[TRADES_COUNT_TOTAL]=Antall%20handler%20totalt
# &header[VWAP_CA]=VWAP&view=DELAYED&source=feed.oax.quotes.INSTRUMENTS
# &filter=ITEM_SECTOR%3D%3DsAEGA.OAX%26%26DELETED!%3Dn1&stop=now
# &start=1501884000000&space=DAY&ascending=true&filename=data.xlsx

# Returns a dataframe (date,start,stop,high,low,volume)
def get_tickerdata_from_osl(ticker, start, end):
	pass