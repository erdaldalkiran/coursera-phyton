spamConfidences = []
fileHandle = open('mbox.txt')
for line in fileHandle:
    if line.startswith('X-DSPAM-Confidence: '):
        index = line.find(':')
        spamConfidence = float(line[index+1:])
        spamConfidences.append(spamConfidence)
if len(spamConfidences) > 0 :
    print 'average spam confidence: ' + str(sum(spamConfidences)/len(spamConfidences))
