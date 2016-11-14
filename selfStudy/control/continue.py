
while True:
    s = input('Enter somethine: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')

print('done: ' + s)

