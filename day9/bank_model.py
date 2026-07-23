from collections import deque


class Account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance


class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []   # sub-branches
        self.accounts = []   # accounts in this branch


    def add_child(self, branch):
        self.children.append(branch)


    def add_account(self, account):
        self.accounts.append(account)


    def total_balance(self):
        # Add accounts in this branch
        total = sum(account.balance for account in self.accounts)

        # Add balances from child branches recursively
        for child in self.children:
            total += child.total_balance()

        return total



# Account transfer graph
# account -> accounts it has paid

transfers = {
    1001: [1002, 1003],
    1002: [1004],
    1003: [1005],
    1004: [],
    1005: []
}



# Breadth First Search

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        account = queue.popleft()

        if account not in visited:
            visited.add(account)

            for neighbour in graph[account]:
                queue.append(neighbour)

    return visited