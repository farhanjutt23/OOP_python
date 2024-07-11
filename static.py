'''this is the staticmethod'''
class emploe:
    company_name="Epis"
    @staticmethod
    def display(name):
        print("The name of the company is the ",emploe.company_name)
        print("my name is the",name)
c=emploe()
c.display("farhan")
