'''constructor in the multi level inheritance '''
class human_being():
    def __init__(self):
        print("Human beging Constructor Called")
        self.name=input("Enter your name ")
class Employee(human_being):
    def __init__(self):
        print("Human beging constructor")
        self.name=float(input("Enter the constructor called"))
class manger(Employee):
    pass
m1=manger()
