

def towerofhanoi(s,d,e,n):
    if n <= 0:
        return

    towerofhanoi(s,e,d,n-1)
    print('Move disk', n, 'from', s, 'to', d)
    towerofhanoi(e,d,s,n-1)


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def bubblesortrec(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    bubblesortrec(arr, n-1)


def printtable(n):
    for i in range(1,11):
        print(n, '*', i, '=', n*i)

def printtablerecur(n, i=0):
    if i > 10:
        return
    print(n, '*', i, '=', n * i)
    printtablerecur(n, i+1)


def fib(n):
    a = 1
    b = 1
    for c in range(3, n+1):
        c = a + b
        a = b
        b = c

    return c

def fibdp(n):
    arr = [0] * (n+1)

    arr[1], arr[2] = 1,1

    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]


    return arr[-1]

def fibrec(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)



def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a

    temp = power(a, b//2)
    res = temp * temp
    if b % 2 == 1:
        res *= a

    return res



s = 's'
e = 'e'
d = 'd'
n = 2
# towerofhanoi(s,d,e,n)
# bubblesortrec([10,9,8,7,6,5,4,3,2,1], 10)
# printtablerecur(5)
print(fib(9))
print(power(2,1000))

