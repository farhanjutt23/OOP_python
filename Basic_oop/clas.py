"""write a program to multiple of the any two numbers ann get the input from the user """
class mul:
    def __init__(self):
        self.n1=0
        self.n2=0
    def mu(self):
        self.n1=int(input("Enter a number"))
        self.n2=int(input("Enter the second number"))
        multiple=self.n1*self.n2
        print("The Multiple of the any two number is the",multiple)
s1=mul()
s1.mu()


