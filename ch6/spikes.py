fruit = 'banana'
print fruit[:]

def characterCounter(stringValue, charValue):
    count = 0

    for char in stringValue:
        if char == charValue:
            count +=1

    return count

print characterCounter('erdal was here!', 'e')
print
#print type(fruit)
#methodNames = dir(str)
#for methodName in methodNames:
#    print methodName

print fruit.capitalize()
print

formatting = '%d integer %g float? %s string' % (5.77, 6.66,  'erdal')
print formatting
print
