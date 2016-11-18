class Robot:
    """
    Represents a robot, with a name
    """

    # class variable
    population = 0


    def __init__(self, name):
        """
        Initialize the data.
        :param name: name of robot.
        """
        self.name = name
        print("(Initializing {})".format(self.name))

        # Robot population +1
        Robot.population += 1

    def die(self):
        """
        I am dying.
        :return:
        """
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was last robot".format(self.name))
        else:
            print("There are still {:d} are working".format(Robot.population))


    def say_hi(self):
        """
        Greeting by Robot
        Yeah, they can do that
        :return:
        """
        print("Greetings, my masters call me {}".format(self.name))

    # #############################################################
    @classmethod
    def how_many(cls):
        """
        Prints the current population
        :return:
        """
        print("We have {:d} robots".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("Destroy robots")
droid1.die()
droid2.die()

Robot.how_many()


