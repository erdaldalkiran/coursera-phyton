import re

days = {}
fileHandle = open('mbox-short.txt')
for line in fileHandle:
	day = re.findall('^From\s\S*\s(\S*)\s', line)
	if len(day) > 0:
		days[day[0]] = days.get(day[0], 0) + 1

print days 