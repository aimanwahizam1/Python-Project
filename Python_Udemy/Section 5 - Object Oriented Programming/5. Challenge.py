# For this challenge, create a bank account class that has two attributes:

# owner
# balance

# and two methods:

# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"
    
    def deposit(self, value):
        self.balance += value
        print(f"Deposit successful.\nCurrent Balance: {self.balance}")

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            print(f"Withdraw successful.\nCurrent Balance: {self.balance}")

        else:
            print(f"Insufficient amount.\nCurrent Balance: {self.balance}")

aiman_account = Account("Aiman Wahizam", 100)

print(aiman_account)

aiman_account.deposit(100)

aiman_account.withdraw(150)
aiman_account.withdraw(100)
