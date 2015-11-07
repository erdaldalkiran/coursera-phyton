import re

tupleVar = ('erdal', 'was','here')
print tupleVar
tupleVar2 = ('erdal',)
print tupleVar2
tupleVar3 = tuple('erdal')
print tupleVar3
#syntax error
#tupleVar4 = tuple('erdal', 'was','here')
tupleVar4 = tuple(['erdal', 'was','here'])
print tupleVar4
#NOTE TO MYSELF give a list of something to tuple function

txt = 'but soft what light in yonder window breaks'
words = re.findall('\S+', txt)
lengthAndWords = []
for word in words:
	lengthAndWords.append((len(word),word))

lengthAndWords.sort(reverse=True)

result = []
for length, word in lengthAndWords:
	result.append(word)
	
print result

dictionary = {'a':10, 'b':1, 'c':22}
items = dictionary.items()
items.sort()
for key,value in items:
	print key, value
