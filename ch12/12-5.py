import socket
import re

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('www.py4inf.com', 80))
mySocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.1\n\n')

retrievedData = ''
while True:
	data = mySocket.recv(5000)
	if len(data) < 1:
		break
	retrievedData += data

content = re.findall('\r\n\r\n([\s\S]*)', retrievedData)
print content[0]

mySocket.close()