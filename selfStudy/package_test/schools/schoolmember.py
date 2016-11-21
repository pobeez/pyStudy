class SchoolMember:
    """
    Represent any school member.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialize school memger: {}".format(self.name))

    def tell(self):
        """
        Tell my details
        """
        print("Name:\"{}\", Age:\"{}\"".format(self.name, self.age))