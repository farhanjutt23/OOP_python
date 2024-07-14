class Employe:
    def __init__(self,sal,ag):
        self.salary=sal
        self.age=ag
    def display(self):
        print(f"the salary of the {self.salary} the age of the emplye is the {self.age}")

    
e=Employe(340000,9)
f=Employe(500000,32)
print(e.age)
print(f.age)
e.display()



