from bank_model import *


# ==========================
# Branch Tree Test
# ==========================

head = Branch("Head Office")

region1 = Branch("Region 1")
region2 = Branch("Region 2")

branch1 = Branch("Branch 1")

head.add_child(region1)
head.add_child(region2)

region1.add_child(branch1)


account1 = Account(1001, "Sara", 5000)
account2 = Account(1002, "John", 3000)
account3 = Account(1003, "Abel", 2000)
account4 = Account(1004, "Mimi", 4000)


head.add_account(account1)
region1.add_account(account2)
region2.add_account(account3)
branch1.add_account(account4)


print("Total Bank Balance:")
print(head.total_balance())



# ==========================
# BFS Test
# ==========================

print("\nAccounts reachable from 1001:")
print(bfs(transfers, 1001))



# ==========================
# 1. Binary Search Tree
# ==========================


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root



def inorder(root):

    if root:

        inorder(root.left)

        print(root.value, end=" ")

        inorder(root.right)



root = None

values = [50, 30, 70, 20, 40, 60, 80]


for value in values:
    root = insert(root, value)


print("\n\nBST In-order:")
inorder(root)



# ==========================
# 2. Tree Height
# ==========================


def height(node):

    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)



print("\n\nTree Height:")
print(height(root))



# ==========================
# 3. DFS
# ==========================


def dfs(graph, start, visited=None):

    if visited is None:
        visited = set()


    visited.add(start)


    for neighbour in graph[start]:

        if neighbour not in visited:
            dfs(graph, neighbour, visited)


    return visited



print("\nDFS Result:")
print(dfs(transfers, 1001))



# ==========================
# 4. Priority Queue
# ==========================

import heapq


tasks = []


heapq.heappush(tasks, (3, "Check account"))
heapq.heappush(tasks, (1, "Emergency transfer"))
heapq.heappush(tasks, (2, "Deposit money"))
heapq.heappush(tasks, (5, "Print report"))
heapq.heappush(tasks, (4, "Send message"))



print("\nPriority Queue:")

while tasks:

    priority, task = heapq.heappop(tasks)

    print(priority, task)