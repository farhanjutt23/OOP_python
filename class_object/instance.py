class stu:
    def __init__(self,nm,m):
        self.name=nm
        self.marks=m
    def display(self):
        print(self.name,self.marks)
std1=stu("farhan",78)
std2=stu("Ali",678)
#out side the class the varibele
std1.name="ahmad"
print(std1.marks,std1.name)
std1.display()
        