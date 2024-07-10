class employe:
    comapny_name="info"  #class variable
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
e1=employe("Farhan",50000)
e2=employe("Vijaye",6777)
print(employe.comapny_name)
print(e1.comapny_name)
employe.comapny_name="TCS"
print(employe.comapny_name)