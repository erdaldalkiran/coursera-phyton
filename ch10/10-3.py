import re

fileHandle = open('mbox.txt')
lettersAndCount = {}

for line in fileHandle:
	letters = re.findall('[a-zA-Z]', line)
	for letter in letters:
		letterInLowerCase = letter.lower()
		lettersAndCount[letterInLowerCase] = lettersAndCount.get(letterInLowerCase, 0 ) + 1

countAndLetter = []
for letter,count in lettersAndCount.items():
	countAndLetter.append((count, letter))

countAndLetter.sort(reverse = True)

for count, letter in countAndLetter:
	print letter, count
