file = open('selskapsliste_uformatert.txt', 'r')
result = open('selskapsliste_formatert.txt', 'w')
line = ''
i = 0
end = False

for currentLine in file:
	stripped = currentLine.rstrip()

	# We only want the first two fields
	if i<2:
		line += stripped + ','
	i += 1
	yesNoString = stripped.lower().startswith(('ja','nei'))
	
	# The last fields always starts with yes or no
	if yesNoString:
		end = True

	# If we have previously had a yes/no string and this is not,
	# then this is the start of a new entry
	if end and (not yesNoString):
		result.write(line.rstrip(', ').lstrip(', ') + '\n')
		line = stripped + ','
		i = 0
		end = False
