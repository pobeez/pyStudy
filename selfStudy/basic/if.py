# if문 예제
number = 23
# python 2 => raw_input, python3 => input
guess = int(input('Enter an integer: '))

if guess == number:
    # new block start here
    print('Congraturations, you guessed it')
    print('(but you do not win any prizes!)')
elif guess > number:
    print('No, it is a little higher than that')
else:
    print('No is is a little lower than that')

print('Done')
