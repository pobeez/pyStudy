class ShortInputException(Exception):
    """
    User defined exception class
    """
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input("Enter a text: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Why did you do and EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
except ShortInputException as ex:
    print("ShortInputException: The input was "\
            "{0} long, expected at least {1}".format(ex.length, ex.atleast))
else:
    print("You entered.. {}".format(text))

