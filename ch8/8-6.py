numbers = []
while True:
    input = raw_input('Enter a number: ')
    if input == 'Done': break
    try:
        number = int(input)
        numbers.append(number)
    except Exception as e:
        print('Please enter a number or type "Done" to end!')
        print e

numbers.sort()
if len(numbers) == 0 : exit()
print 'Minimum: ' + str(numbers[0])
print 'Maximum: ' + str(numbers[len(numbers)-1])
