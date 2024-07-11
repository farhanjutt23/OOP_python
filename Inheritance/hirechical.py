'''one pasrents class has many child class'''
class person:
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    def display1(self):
        print("This is person display")
class employe(person):
    def __init__(self, nm, ag,sal):
        super().__init__(nm, ag)
        self.salary=sal
    def display2(self):
        print("This is employe display")
class student(person):
    def __init__(self, nm, ag,m):
        super().__init__(nm, ag)
        self.marks=m
    def display3(self):
        print("This is student  display")
p=person("Farhan",21,99)
e=employe("jay",21,99)
s=student("Farhan",21,66)
s.display1()


