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

#show balance
print(f"{account1.owner}'s balance: {account1.balance}")
print(f"{account2.owner}'s balance: {account2.balance}")
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

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")


class SavingsAccount(Account):
    def __init__(self, owner, account_number, rate, balance=0):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print("=== Savings Account ===")
        super().statement()


class CurrentAccount(Account):
    def __init__(self, owner, account_number, overdraft, balance=0):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < -self.overdraft:
            print("Overdraft limit exceeded.")
        else:
            self._Account__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def statement(self):
        print("=== Current Account ===")
        super().statement()


# ----------------------------
# Test the program
# ----------------------------

# Savings Account
savings = SavingsAccount("Eftu", "1001", 0.05, 1000)

savings.deposit(500)
savings.add_interest()
savings.statement()

print()

# Current Account
current = CurrentAccount("Sara", "1002", 500, 300)

current.withdraw(700)
current.statement()

print()

# Polymorphism
accounts = [savings, current]

print("=== All Accounts ===")
for account in accounts:
    account.statement()
    print()