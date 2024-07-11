class father:
    def __init__(self):
        print("Father is the constractoe")
        self.vehil="sector"
class child(father):
    pass
c=child()
print(c.vehil)
