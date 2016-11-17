def print_max(x, y):
    """Prints the maximum of tow integers

    :param x: integer
    :param y: integer
    :return: maximum value
    """
    x = int(x)
    y = int(y)
    if x > y:
        return x
    elif x == y:
        return 'Numbers are equal'
    else:
        return y

print(print_max(1, 3))
print(print_max(2, 2))
print(print_max(4, 3))
# Print DocStrings
#print(print_max.__doc__)

help(print_max)