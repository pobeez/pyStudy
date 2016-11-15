x = 50

def func1():
    global x
    print('x is ', x)
    x = 2
    print('Global x is changed to ', x)


func1()

print('x is ', x)
