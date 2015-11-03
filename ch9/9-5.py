import re

schools = {}
fileHandle = open('mbox-short.txt')

for line in fileHandle:
	schoolList = re.findall('^From\s\S+?@(\S+)\s', line)
	if len(schoolList) > 0:
		school = schoolList[0]
		schools[school] = schools.get(school, 0) + 1

print schools