import socket
import sys
url = raw_input('Website to open? ')
try:
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.settimeout(5)
	print mySocket.gettimeout()
	mySocket.connect((url, 80))
	
	mySocket.send('GET http://'+url+'/ HTTP/1.0\n\n')
	
	while True:
		data = mySocket.recv(512)
		if len(data) < 1:
			break
		print data
	
	mySocket.close()
except socket.gaierror as inst:
	print type(inst)
	print inst
except:
	print "Unexpected error:", sys.exc_info()[0]
	raise
