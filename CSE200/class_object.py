class Student:
    def __init__(self, f_name, l_name, id, cgpa, dept):
        self.f_name = f_name
        self.l_name = l_name
        self.id = id
        self.cgpa = cgpa
        self.dept = dept

    def fullname(self):
        print(self.f_name + " " + self.l_name)

s1 = Student("Riyad", "Hasan",  2238478, 2, "CSE")
s2 = Student("Alvee", "Sarker", "2311249", 2, "CSE")

