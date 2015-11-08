import re



while True:
	count = 0
	
	regexp = raw_input('Enter a regular expression: ')
	if regexp == 'quit':
		break
	
	fileHandle = open('mbox.txt')
	
	for line in fileHandle:
		if  re.search(regexp, line) :
			count += 1
	
	print 'mbox.txt had '+ str(count) +' lines that matched ' + regexp 
	