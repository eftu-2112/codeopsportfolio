class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


# Create two accounts
account1 = Account("Eftu", "1001", 1000)
account2 = Account("Sara", "1002", 500)

# Transactions
account1.deposit(300)
account1.withdraw(200)

account2.deposit(-50)
account2.withdraw(700)

# Show balances
print(f"{account1.owner}'s balance: {account1.balance}")
print(f"{account2.owner}'s balance: {account2.balance}")