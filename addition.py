"""write a program that the add the any two number in the class"""
class number:
    def __init__(self):
        self.x=int(input("Enter the first number"))
        self.y=int(input("Enter the second number"))
       
    def display(self):
        print("The first number is the ", self.x)
        print("The second number is the ", self.y)
    def cal(self):
        print("The sum of these number is the ", self.x+self.y)

c=number()
t=number()
c.display()
c.cal()
t.display()
t.cal()

