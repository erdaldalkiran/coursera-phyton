import urllib

url = raw_input('Website to open? ')

try:
	urlHandle = urllib.urlopen('http://' + url+'/')
	totalRetrievedDataLength = 0
	while True:
		data = urlHandle.read(500)
		if len(data) < 1:
			break
		totalRetrievedDataLength += len(data)
		if totalRetrievedDataLength <= 3000:
			print data
	
	print totalRetrievedDataLength
except:
	print 'something went wrong'
	raise