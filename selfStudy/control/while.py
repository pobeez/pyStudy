# 2016.11.14 whie문

number = 23

running = True

while running:
    guess = int(input('Type number: '))

    if guess == number:
        print('Congraturations, you guessed it')
        running = False
        break
    elif guess < number:
        print('Input number is a little lower than number')
    else:
        print('Input number is a little higher than number')
else:
    print('Loop is end!')

print('Done')
