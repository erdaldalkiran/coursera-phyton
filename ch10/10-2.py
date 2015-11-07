import re

fileHandle = open('mbox-short.txt')
hoursInDict = {}
for line in fileHandle:
	hours = re.findall('^From\s.*\s([0-9]{2}):', line)
	if len(hours) > 0:
		hoursInDict[hours[0]] = hoursInDict.get(hours[0], 0) + 1
sortedKeys = hoursInDict.items()
sortedKeys.sort()
for key, value in sortedKeys:
	print key,value