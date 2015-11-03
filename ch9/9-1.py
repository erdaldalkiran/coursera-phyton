import re

wordCounts = {}
fileHandle = open('words.txt')
for line in fileHandle:
	wordsInLine = re.findall('[a-zA-Z]+', line)
	for word in wordsInLine:
		lowerCaseWord = word.lower()
		wordCounts[lowerCaseWord] = wordCounts.get(lowerCaseWord, 0) + 1

keys = wordCounts.keys()
keys.sort()

for key in keys:
	print key +': '+ str(wordCounts[key])