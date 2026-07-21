class BankConfig:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.interest_rate = 0.05
            cls.__instance.overdraft_limit = 1000
        return cls.__instance


# ---------------- Observer ----------------

class SMSAlert:
    def update(self, message):
        print("SMS:", message)


class AuditLog:
    def update(self, message):
        print("Audit:", message)


# ---------------- Account ----------------

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []

    @property
    def balance(self):
        return self.__balance

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.notify(f"{self.owner} deposited {amount} ETB")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.notify(f"{self.owner} withdrew {amount} ETB")
        else:
            print("Invalid withdrawal.")

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} ETB")


# ---------------- Savings ----------------

class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self.rate = BankConfig().interest_rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    def statement(self):
        print("=== Savings Account ===")
        super().statement()


# ---------------- Current ----------------

class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft:
            self._Account__balance -= amount
            self.notify(f"{self.owner} withdrew {amount} ETB")
        else:
            print("Overdraft limit exceeded.")

    def statement(self):
        print("=== Current Account ===")
        super().statement()


# ---------------- Factory ----------------

class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Unknown account type")


# ---------------- Test ----------------

sms = SMSAlert()
audit = AuditLog()

acc1 = AccountFactory.create("savings", "Eftu", "1001", 1000)
acc2 = AccountFactory.create("current", "Sara", "1002", 500)

acc1.subscribe(sms)
acc1.subscribe(audit)

acc2.subscribe(sms)
acc2.subscribe(audit)

acc1.deposit(500)
acc1.add_interest()
acc1.statement()

print()

acc2.withdraw(1200)
acc2.statement()
config1 = BankConfig()
config2 = BankConfig()

print(config1 is config2)