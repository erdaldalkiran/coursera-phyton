value = 'X-DSPAM-Confidence: 0.8475'
colonPos = value.find(':')
floatAsStr = value[colonPos+2:]
print float(floatAsStr)
print
