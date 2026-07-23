class AccountRegistry:

    def __init__(self):
        # account number -> account object
        self.by_number = {}

        # keep insertion order
        self.order = []


    def add(self, acc):
        self.by_number[acc.account_number] = acc
        self.order.append(acc.account_number)


    def find(self, number):
        return self.by_number.get(number)


    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts


    def add_transaction(self, acc, transaction):
        if not hasattr(acc, "history"):
            acc.history = []

        acc.history.append(transaction)


    def undo_last(self, acc):

        if len(acc.history) == 0:
            print("No transaction to undo")
            return

        last = acc.history.pop()

        if last["type"] == "deposit":
            acc.balance -= last["amount"]

        elif last["type"] == "withdraw":
            acc.balance += last["amount"]

        print("Undo:", last)