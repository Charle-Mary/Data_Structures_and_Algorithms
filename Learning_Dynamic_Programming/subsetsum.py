def subsetsum(arr,x,path=""):
    if x == 0:
        return True
    if not arr:
        return False
    if arr[0] > x:
        return subsetsum(arr[1:], x)
    return subsetsum(arr[1:], x-arr[0]) or subsetsum(arr[1:], x)


def subsetsumdp(arr, x):
    m = len(arr)
    cache = [[0 for j in range(x+1)] for i in range(m+1)]
    for i in range(m+1):
        cache[i][0] = True

    for j in range(1, x+1):
        cache[0][j] = False

    for i in range(1, m+1):
        for j in range(1, x+1):
            if arr[i-1] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j - arr[i-1]] or cache[i-1][j]

    if cache[-1][-1]:
        while x > 0 or m > 0:
            if cache[m][x] == cache[m-1][x]:
                m -= 1
            else:
                print("We need item", arr[m-1])
                x -= arr[m-1]
                m -= 1
    return cache[-1][-1]



arr = [4,3,4,5,5,7,8,2,3,1]
x = 30
print(subsetsum(arr, x))
print(subsetsumdp(arr,x))