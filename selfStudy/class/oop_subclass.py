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

class Teacher(SchoolMember):
    """
    Represent a teacher
    """
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialize teacher: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: \"{}\"".format(self.salary))

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

t = Teacher("Sungjin Moon", 40, 6000000)
s = Student("Wonjae Moon", 14, 100)
print()
member = [t, s]

# 다형성 자식 클래스는 부모클래스의 멤버를 호출학 수 있다.
for m in member:
    m.tell()
