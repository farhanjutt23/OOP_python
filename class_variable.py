'''there is the class variable in which we can use the value and store the values'''
class Employe:
    company_name="Mk sons"
    def __init__(self,sal,ag):
        self.salary=sal
        self.age=ag
e=Employe(39999,32)
print(e.age)
print(e.company_name)