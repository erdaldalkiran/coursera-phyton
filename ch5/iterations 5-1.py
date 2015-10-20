total = 0
count = 0
while True:
    input = raw_input('> ')
    if input == 'done':
        break

    try:
        total += int(input)
        count += 1
    except Exception as e:
        print 'bad, bad boy!'

print total
if count > 0:
    print count, total/float(count)
