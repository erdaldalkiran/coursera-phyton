import urllib
import re

url = raw_input('Website to open?\n')

try:
	data = urllib.urlopen('http://'+url+'/').read().lower()
	print data
	matches = re.findall('<p[\s\S]*?>[\s\S]*?<\/p>', data)
	
	for match in matches:
		print match
	
	totalCountOfParagraphs = len( matches)

	print totalCountOfParagraphs
except:
	print 'Something went wrong'
	raise