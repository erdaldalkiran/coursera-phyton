import re

senders = {}
fileHandle = open('mbox.txt')

for line in fileHandle:
	senderList = re.findall('^From\s(\S+)\s', line)
	if len(senderList) > 0:
		sender = senderList[0]
		senders[sender] = senders.get(sender, 0) + 1

maxEmailSentCount = 0
maxEmailSender = None

for sender in senders:
	if senders[sender] > maxEmailSentCount:
		maxEmailSentCount = senders[sender]
		maxEmailSender = sender
		
print maxEmailSender, maxEmailSentCount