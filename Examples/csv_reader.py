import csv
with open('aker.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	next(reader, None) # Skip header
	for row in reader:
		print row