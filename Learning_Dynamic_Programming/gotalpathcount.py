def numOfPaths(m,n):
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return 1

    return numOfPaths(m-1, n) + numOfPaths(m, n-1)

def numOfPathsdp(m,n):
    cache = [[0 for x in range(n+1)] for y in range(m+1)]

    for j in range(1, n+1):
        cache[0][j] = 1

    for i in range(1, m+1):
        cache[i][0] = 1

    print(cache)

    for i in range(1, m+1):
        for j in range(1, n+1):
            cache[i][j] = cache[i-1][j] + cache[i][j-1]

    return cache[m][n]



print(numOfPathsdp(2,3))
print(numOfPaths(2,3))