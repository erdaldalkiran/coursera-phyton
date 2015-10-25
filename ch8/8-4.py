words = []
fileHandle = open('romeo.txt')
for line in fileHandle:
    splittedWords = line.split()
    for splittedWord in splittedWords:
        if not splittedWord in words:
            words.append(splittedWord)
words.sort()
print words
