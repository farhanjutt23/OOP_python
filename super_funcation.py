'''by using the super() we can acess the propertites of the parents class'''
class commputer:
    def __init__(self,rm,st):
        self.ram=rm
        self.storage=st
        print("this is the paents class")
class mobile(commputer):
    def __init__(self,rm,st):
      super().__init__(rm,st)
      self.model="I phone"
      print("this is the child class")
c=mobile(45,54)
print(c.__dict__)