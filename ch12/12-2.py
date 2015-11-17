import socket

url = raw_input('Website to open? ')
try:
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.settimeout(5)
	mySocket.connect((url, 80))
	mySocket.send('GET http://'+url+'/ HTTP/1.0\n\n')
	
	totalRetrievedDataLength = 0
	while True:
		data = mySocket.recv(500)
		if len(data) < 1:
			break
		totalRetrievedDataLength += len(data)
		if totalRetrievedDataLength <= 3000:
			print data
	
	print totalRetrievedDataLength
		
	
except Exception as exp:
	print exp
	raise
	