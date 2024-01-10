#7/23/22

"""
            ---------- Task One ----------
    -Declare class and give it the name "User" - Check
    -The __init__ method has parameters defined as
    (self, name, pin, password)
    - The attribute of the User class are defined as
    name, pin, and password
"""


class User:
    def __init__(self, name: str, pin: int, password: str):
        self.name = name
        self.pin = pin
        self.password = password


    """
            ---------- Task Two ----------
        The "User" class should have three methods:
            *change_name - changes the name of User
            *change_pin - changes the PIN code of User
            *change_password - changes the password of User
    """

    def change_name(self, new_name: str):
        self.name=new_name              #python: self.  == java: this.

    def change_pin(self, new_pin: int):
        self.pin=new_pin

    def change_password(self, new_password: str):
        self.password = new_password

"""
            ---------- Task three ----------
    -Declare a class and give it the name "BankUser"
   -"BankUser" class will inherit the "User" class
   -The __init__ method has parameter defined as
    (self, name, pin, password)
   -The super method has parameters defined as
    (name, pin, password)
   -The attributes of the "BankUser" is balanced with
    a default value of zero
"""

class BankUser(User):
    def __init__(self, name: str, pin:int, password:str):
        super().__init__(name, pin, password)
        self.balance = 0.00

    def print_name(self):
        print(self.name)

    """
            ---------- Task Four ----------
        The "BankUser" class should have three methods:
            *show_balance - prints the balance of the User
            *withdraw - withdrawing money decreses the account balance
            *deposit - depositing money increases the account balance
    """

    def show_balance(self, string_variable: str):
        print(f"{self.name}, your balance {string_variable}: ${self.balance:.2f}")

    def withdraw(self, withdraw_amount: float):
        if withdraw_amount > self.balance:
            print(f"You requested amount of: ${withdraw_amount:.2f} is greater than {self.balance}.")
            print(f"Please request an amount below: ${self.balance}.")
        else:
            if withdraw_amount % 20 == 0:
                self.show_balance("was")
                self.balance -= withdraw_amount
                self.show_balance("is now")         #self. calls show_balance inside the withdraw method
            else:
                print("You must request the amount in $20 increments.")

    def deposit(self, deposit_amount: float):
        if deposit_amount > 0:
            if deposit_amount %20 == 0:
                self.show_balance("was")
                self.balance += deposit_amount
                self.show_balance("is now")
            else:
                print("--")
        else:
            print("We do not allow negative deposits.")

    """
            ---------- task five ----------
    create two or more methods for the BankUser class:
        *transfer_money
            -transfers money to another user if
            -correct PIN
        *request_money
    """

    def transfer_money(self, user: object, amount: float):
        print(f"You are transferring ${amount:.2f} to {user.name}")
        print("Authentication Required:")
        pincode = int(input(f"Please input {self.name}'s pin:"))

        if self.pin == pincode:
            print("Transfer Authorized")

            #self.balance -= amount
            self.withdraw(amount)
            #user.balance += amount
            user.deposit(amount)

            print(f"The transfer of {amount} to {user.name} is complete")
            self.show_balance("is")

    def request_money(self, user, amount: float):
        print(f"You are requesting ${amount:.2f} from {user.name}")
        print("Authentication Required:")

        while True:
            pincode = input("Please input {user.name}'s pin: ")
            if pincode.isnumeric():
                pincode = int(pincode)
                if pincode == user.pin:
                    break
                else:
                    print("pin is incorrect")
            else:
                print("Pin must be an integer.")

        #print(pincode.isnumeric(), isinstance(pincode, int), isinstance(pincode, str))      #True False True -> pin is numeric and a string

        while True:
            password = input(f"Please enter the password for {self.name}: ")

            if self.password == password:
                print("Transfer Authorized")
                if amount %20 == 0:
                    user.withdraw(amount)
                    self.deposit(amount)

                    print(f"The request for ${amount:.2f} is complete. ")
                    self.show_balance("is")
                else:
                    print("However, you must request money in $20")
                break


#user1 = User("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)
#print()

#user2 = BankUser("Bill", 7777, "Password")
#user2.print_name()

"""
def test():
    user12 = User("Bob", 1234, "password")
    print(user12.name, user12.pin, user12.password)
    user12.change_name("Bobby")
    user12.change_pin(4321)
    user12.change_password("newpassword")
    print(user12.name, user12.pin, user12.password)

#test()

bankuser1 = BankUser("Bob", 1234, "password")
bankuser1.show_balance()
bankuser1.deposit(1000.0)
#bankuser1.show.balance()
bankuser1.withdraw(500.0)
#bankuser1.show_balance()
"""


"""Driver code for task five"""
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000)
#bankuser2.show_balance()
#bankuser1.show_balance()
print()

bankuser2.transfer_money(bankuser1, .500)
#bankuser2.show_balance()
#bankuser1.show_balance()
"""driver code for task five end"""
