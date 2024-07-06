'''create student class that takes name & marks of 3 subjects as arguments 
in the consdtructor then create a method of the averge of the subjects'''
class student:
    def __init__(self,sname,computer,math,english):
        self.name=sname
        self.marks1=computer
        self.marks2=math
        self.marks3=english
    def averge(self):
        sum=self.marks1+self.marks2+self.marks3
        avg=sum/3
        print("The averge of the numbers is the ",avg)
        

s1=student("M Farhan ur rasool",72,93,90)
print(s1.name,s1.marks1,s1.marks2,s1.marks3)
s1.averge()


        