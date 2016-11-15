def abc_print(a, b = 5, c = 10):
    print("{_0}, {_1}, {_2}".format(_0 = a, _1 = b, _2 = c))

abc_print(10, 30, 40)
abc_print(c=100, a=30)
abc_print(3000, c=20000)
