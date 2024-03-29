"""everything is an object in Python
real-world applications mei kaam aata hai 

Generality to Specificity - apne khud ke data types banaa rhe ho 

6 parts - 
Class
Object
Inheritance
Abstraction
Inheritance
Encapsulation
Polymorphism

 - Object kisi class ka hi hota hai
 - Data type hota h class - aur uss data type ka variable is called an object


syntax : 

class <name> {name should be in Pascal case - ThisIsPascalCase}:
    vars = "value"
    def function_name(): {snake case hai ye - } 


OBJECT LITERALS (object banaane ak asaan treeka) : 

what is method - a special function written inside a class
function is a normal function (not inside class)

object = class()

"""


class AtmMachine :
    def __init__(self):
        #jab bhi variable declare honge, iske andar honge
        #__init__ is a constructor
        #constructor is a special method jo automatically execute hoga jab ye class ka object banegaa
        #constructor ka control user ke paas nahi hai
        # self - SBI hi self hai
        # har alag instance ke liye we'll have different values
        # wo saare instances hi self hain

        #class ka koi bhi object in variables ko access krke change krr skta hai. Which is not good
        self.__pin = ""
        self.__balance = 0

        # variable will be stored in the form of : _AtmMachine__balance
        #nothing in Python is truly private

        self.__cashAmount = 200000
        self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if new_pin.isnumeric() and len(new_pin) == 4:
            print("PIN changed")
            print("\n")
        else:
            print("Try Again!")
            print("\n")


    def menu(self):
        user_input = input(
            """How would you like to proceed?
            1. Enter 1 to create PIN
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
            """)
        print("\n")

        if user_input == '1':
            print('Create Pin')
            self.create_pin()
            self.menu()
        elif user_input == '2':
            print('Deposit')
            self.deposit()
            self.menu()
        elif user_input == '3':
            print('Withdraw')
            self.withdraw()
            self.menu()
        elif user_input == '4':
            print('Balance')
            self.check_balance()
            self.menu()
        elif user_input=='5':
            print('Exit')
        else:
            print("Invalid Input")
            self.menu()
    





    def create_pin(self):
        self.__pin = input("Enter your PIN - ")
        if self.__pin.isnumeric() and len(str(self.__pin)) == 4:
            print("PIN set successfully")
            print("\n")
        else:
            print("Try Again. PIN must be 4 char long")
            print("\n")
            self.create_pin()

        print("Your new PIN is - ", self.__pin)


    def deposit(self):
        temp = input("Enter your PIN - ")
        if temp == self.__pin:
            amount=int(input("Enter the amount to deposit - "))
            self.__balance = self.__balance + amount
            print("Your new balance is - ", self.__balance)
        else:
            print("Invalid PIN. Try again!")
    

    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn - "))
        if self.__cashAmount >= amount and amount <=self.__balance:
            temp = input("Enter your PIN: ")
            if temp == str(self.__pin):
                self.__cashAmount -= amount
                self.__balance -= amount
                print("Withdrawal successful. New balance is ", self.__balance)
            else:
                print("Invalid request!")
        else:
            print("Not enough balance available!")


    def check_balance(self):
        temp = input("Enter your PIN - ")
        if temp == self.__pin:
            print("Your current balance is - ", self.__balance)
        else:
            print("Invalid PIN!")

SBI = AtmMachine()