'''in the heritance we can called the parents class through the child class'''
class employe:    #parents class
    bouns=4000
    def display(self):
        print("This is the display method")
class manger(employe):    #child class
    bouns1=57888
    def show(self):
        print("There is show the manger class")
e1=employe()
e2=manger()
e1.display()
print(e2.bouns)


