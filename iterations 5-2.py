numbers = []
while True:
    input = raw_input('> ')
    if input == 'done':
        break

    try:
        numbers.append(int(input))
    except Exception as e:
        print 'bad, bad boy!'

if len(numbers) > 0:
    print max(numbers), min(numbers), sum(numbers)/float(len(numbers))
