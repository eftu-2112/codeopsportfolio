def getOnlyEvens(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
         result.append(arr[i])
    print(result)
getOnlyEvens([1, 2, 3, 6, 4, 8])
getOnlyEvens([0, 1, 2, 3, 4])  
#qu2
def reversecompare(num):
    reversed_num=int(str(num)[::-1])
    if num > reversed_num:
        print("ok")
    else:
        print("not ok")

reversecompare(72)
reversecompare(23)
#qu3
def returnFactorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))

#qu4
def checkMeera(arr):
    for n in arr:
        if n * 2 in arr:
            print("I am NOT a Meera array")
            return

    print("I am a Meera array")


# Test Cases
checkMeera([10, 4, 0, 5])
checkMeera([7, 4, 9])
checkMeera([1, -6, 4, -3])

#qu5
def isDual(arr):
    for num in arr:
        if arr.count(num) != 2:
            return 0

    return 1


# Test Cases
print(isDual([1, 2, 1, 3, 3, 2]))
print(isDual([2, 5, 2, 5, 5]))
print(isDual([3, 1, 1, 2, 2]))
#qu6
def returnFactorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# Test Cases
print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))