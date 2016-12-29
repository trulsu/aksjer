from pandas_datareader import data

aker = data.DataReader('AKSO.OL', 'yahoo', '2016-01-01', '2016-01-10')

print aker.head()
print aker.tail()

# Save as CSV
aker.to_csv('aker.csv')

# Format:
# ---------
# Date (yyyy-mm-dd)
# Open
# High
# Low
# Close
# Volume
# Adj Close