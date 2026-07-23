# Recursive Sum

def total(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + total(nums[1:])

print(total([1, 2, 3, 4, 5]))


# Count Down

def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)

count_down(5)


# Binary Search

def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

numbers = [2,4,6,8,10,12]
print(binary_search(numbers,8))


# Merge Sort

def merge_sort(items):
    return sorted(items)

print(merge_sort([9,5,3,1,7]))


# Sort with Key

accounts = [
    ("Sara",1500),
    ("John",3000),
    ("Abel",1000)
]

print(sorted(accounts,key=lambda x:x[1],reverse=True))


# Two Pointers

def has_pair(nums,target):
    left=0
    right=len(nums)-1

    while left<right:
        s=nums[left]+nums[right]

        if s==target:
            return True

        elif s<target:
            left+=1

        else:
            right-=1

    return False

print(has_pair([1,2,3,4,5,6],9))