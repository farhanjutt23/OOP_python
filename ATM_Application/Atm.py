class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input(
            """Hii!! how i can help u
            1.Press 1 to create the pin
            2.press 2 to chane the pin
            3.press 3 to check the balnce
            4.press 4 to with drwa
            5. anything else to exist 
            
            
            """)
        if user_input=="1":
           self.create_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input == "3":
             self.check_balance()
        elif user_input =="4":
            #with draw
            pass
        else:
            exit()
    def create_pin(self):
        user_pin=input("Enter the user pin")
        self.pin=user_pin

        user_balance=int(input("Enter The user balance"))
        self.balance=user_balance 
        print("Your Pin is create Sucessfully")
        self.menu()
    def change_pin(self):
        old_pin=int(input("Enter the your old pin"))
        if old_pin==self.pin:
            #change the pin
            new_pin=int(input("Enter the new pin"))
            self.pin=new_pin
            print("your Pin is the change sucessfulyy")
            self.menu()
        else:
            print("NO You cannot do this")
            self.menu()
    def check_balance(self):
        user_pin=int(input("Enter The your pin"))
        if user_pin==self.pin:
            print("Your balnce is the ", self.balance)
        else:
            print("No please get out")

            



S1=Atm()
 

                      