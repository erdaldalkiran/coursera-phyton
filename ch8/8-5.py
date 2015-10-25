froms = []
fileHandle = open('mbox-short.txt')
for line in fileHandle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != "From": continue
    froms.append(words[1])

for fromm in froms:
    print fromm

print len(froms)
