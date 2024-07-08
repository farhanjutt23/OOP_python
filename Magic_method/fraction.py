class frac:
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
    def __str__(self):
      return "{}/{}".format(self.num1,self.num2)
    def __add__(self,other):
        new_num=self.num1*other.num2 + other.num1*self.num2
        new_dem=self.num2*other.num1
        return "{}/{}".format(new_num,new_dem)
    def __mul__(self,other):
        new_num=self.num1*other.num1
        new_dem=self.num2*other.num2
        return "{}/{}".format(new_num,new_dem)
    def __sub__(self,other):
        new_num=self.num1*other.num2 - other.num1*self.num2
        new_dem=self.num2*other.num1
        return "{}/{}".format(new_num,new_dem)
    def __truediv__(self,other):
        new_num=self.num1*other.num2
        new_dem=self.num2*other.num1
        return "{}/{}".format(new_num,new_dem)
fr=frac(3,4)
fr2=frac(4,6)
print(fr)
print(fr2)
print(fr+fr2)
print(fr*fr2)
print(fr-fr2)
print(fr/fr2)

 