def factrecur(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return pow(n,2) * factrecur(n-1)

def factiter(n):
    sum = 1
    for i in range(n, 1, -1):
        sum *= i * i
    return sum



def addsum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        arr[i] = arr[i] + addsum(arr[:i])

    return arr[i]





print(factrecur(5))
print(factiter(5))
X = [1,2,3,4,5,6]
addsum(X)
print(X)
