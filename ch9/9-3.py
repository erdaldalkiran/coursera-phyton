import re

senders = {}
fileHandle = open('mbox-short.txt')

for line in fileHandle:
	senderList = re.findall('^From\s(\S+)\s', line)
	if len(senderList) > 0:
		sender = senderList[0]
		senders[sender] = senders.get(sender, 0) + 1

print senders