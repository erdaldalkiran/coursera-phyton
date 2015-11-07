import re

fileHandle = open('mbox.txt')
senderAndCount = {}

for line in fileHandle:
	senders = re.findall('^From\s(\S*@\S*)\s', line)
	if len(senders) > 0:
		sender = senders[0]
		senderAndCount[sender] = senderAndCount.get(sender, 0) + 1

if len(senderAndCount) == 0:
	print 'No sender is found'
	exit()
	
countAndSender = []
for key,value in senderAndCount.items():
	countAndSender.append((value,key))
countAndSender.sort(reverse = True)

sender, count = countAndSender[0][1], countAndSender[0][0]

print sender, count