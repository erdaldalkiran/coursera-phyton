import re

fileHandle = open('mbox-short.txt')
revisions = []
for line in fileHandle:
	macthes = re.findall('^New\sRevision:\s([0-9]+)', line)
	for match in macthes:
		revisions.append(int(match))

if len(revisions) > 0:
	print sum(revisions) / float(len(revisions))
else:
	print 'No Revision Found!'