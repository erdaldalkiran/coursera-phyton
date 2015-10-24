fileHandle = open('C:\Users\erdal_000\Desktop\mbox.txt')
print fileHandle

content = fileHandle.read()
print 'chars count:'  + str(len(content))
print type(content)
#for line in fileHandle:
#    print line

usersFile = raw_input('Please enter the file name: ')
try:
    handle = open(usersFile)
except Exception as e:
    print e
    pass

outputFileHandle = open('output.txt', 'r+')
print outputFileHandle

outputFileHandle.write('erdal was here!')
outputFileHandle.write('new line?\n')
outputFileHandle.write('use \\n to put new line')

for line in outputFileHandle:
    print line

outputFileHandle.close()
