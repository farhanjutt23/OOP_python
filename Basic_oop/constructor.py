'''there is the constructor in the python that is automaticsly create'''

'''write a program in the python in the consdructor to print the name and the number of the 
student as a permater'''
class stu:
    def __init__(self,sname,smarks):
        self.name=sname
        self.marks=smarks
s1=stu("farhan",90)
print(s1.name,s1.marks)
s2=stu("Ali",34)
print(s2.name,s2.marks)


        