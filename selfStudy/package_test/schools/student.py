from schools.schoolmember import *

class Student(SchoolMember):
    """
    Represent a student
    """
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print("Initialize student: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Mark: \"{}\"".format(self.mark))