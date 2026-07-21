from registry import AccountRegistry


class Account:

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.history = []


    def deposit(self, amount):
        self.balance += amount
        self.history.append(
            {
                "type": "deposit",
                "amount": amount
            }
        )


    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(
            {
                "type": "withdraw",
                "amount": amount
            }
        )



registry = AccountRegistry()


acc1 = Account(1001, "Sara", 1500)
acc2 = Account(1002, "John", 3000)


registry.add(acc1)
registry.add(acc2)


# O(1) search
account = registry.find(1001)

print("Found:")
print(account.owner)
print(account.balance)



# ordered list
print("\nAll Accounts:")

for acc in registry.list_all():
    print(acc.account_number, acc.owner)



# transaction history

acc1.deposit(500)
acc1.withdraw(200)

print("\nBalance before undo:")
print(acc1.balance)


registry.undo_last(acc1)


print("Balance after undo:")
print(acc1.balance)