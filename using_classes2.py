class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)

user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)

user1.change_password("bestpassword")
