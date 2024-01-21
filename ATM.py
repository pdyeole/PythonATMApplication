class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""
                    Hello How Would You Like to Proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    4. Enter 5 to exit
""")

        if user_input == '1':
            self.create_pin()
            # print("Create Pin")
        elif user_input=='2':
            self.deposit()
            # print("Deposit")
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.balance()
        else:
            print("Bye")
            

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your Pin")
        if temp==self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance+amount
            print("Deposit Successfull")
        else:
            print("Invalid Pin")
    
    def withdraw(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount>self.balance:
                print("Insufficient Funds")
            else:
                self.balance = self.balance - amount
        else:
            print("Wrong pin")
    
    def checkBalance(self):
        temp = input("Enter the Pin")
        if self.pin == temp:
            print(self.balance)
        else:
            print("Wrong pin")
    


if __name__=='__main__':
    atm_acc = ATM()
# Functions vs methods 
    