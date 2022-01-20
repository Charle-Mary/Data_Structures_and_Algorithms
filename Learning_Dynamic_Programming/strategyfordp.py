cost = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]

def mincost(cost, m, n):
    if m == 0 and n == 0:
        return cost[0][0]
    if m == 0:
        return mincost(cost, m, n-1) + cost[0][n]
    if n == 0:
        return mincost(cost, m-1, n) + cost[m][0]

    x = mincost(cost, m-1, n)
    y = mincost(cost, m, n-1)

    return min(x,y) + cost[m][n]


mem = [[0 for x in range(len(cost[0]))] for y in range(len(cost))]
def mincostmem(cost, m, n):
    if mem[m][n] != 0:
        return mem[m][n]

    elif m == 0 and n == 0:
        mem[m][n] = cost[0][0]
    elif m == 0:
        mem[m][n] = mincostmem(cost, m, n-1) + cost[0][n]
    elif n == 0:
        mem[m][n] = mincostmem(cost, m-1, n) + cost[m][0]

    else:
        x = mincostmem(cost, m-1, n)
        y = mincostmem(cost, m, n-1)

        mem[m][n] = min(x,y) + cost[m][n]

    return mem[m][n]

cache = [[0 for x in range(len(cost[0]))] for y in range(len(cost))]
def mincostdp(cost):
    cache[0][0] = cost[0][0]

    for j in range(1, len(cost[0])):
        cache[0][j] = cache[0][j-1] + cost[0][j]

    for i in range(1, len(cost)):
        cache[i][0] = cache[i-1][0] + cost[i][0]

    for r in range(1, len(cost)):
        for c in range(1, len(cost[0])):
            cache[r][c] = min(cache[r-1][c], cache[r][c-1]) + cost[r][c]

    return cache[len(cost) - 1][len(cost[0]) - 1]



def mincostdiag(cost, m, n):
    if m == 0 and n == 0:
        return cost[0][0]
    if m == 0:
        return mincostdiag(cost, m, n-1) + cost[0][n]
    if n == 0:
        return mincostdiag(cost, m-1, n) + cost[m][0]

    x = mincostdiag(cost, m-1, n)
    y = mincostdiag(cost, m, n-1)
    z = mincostdiag(cost, m-1, n-1)

    return min(x, y, z) + cost[m][n]

cachediag = [[0 for x in range(len(cost[0]))] for y in range(len(cost))]
def mincostdiagmem(cost, m, n):
    if cachediag[m][n] != 0:
        return cachediag[m][n]

    elif m == 0 and n == 0:
        cachediag[m][n] = cost[0][0]
    elif m == 0:
        cachediag[m][n] = mincostdiag(cost, m, n-1) + cost[0][n]
    elif n == 0:
        cachediag[m][n] = mincostdiag(cost, m-1, n) + cost[m][0]
    else:
        x = mincostdiag(cost, m - 1, n)
        y = mincostdiag(cost, m, n - 1)
        z = mincostdiag(cost, m - 1, n - 1)

        cachediag[m][n] = min(x, y, z) + cost[m][n]
    return cachediag[m][n]

cachedp = [[0 for x in range(len(cost[0]))] for y in range(len(cost))]
def mincostdiagdp(cost):
    cachedp[0][0] = cost[0][0]

    for j in range(1, len(cost[0])):
        cachedp[0][j] = cachedp[0][j-1] + cost[0][j]

    for i in range(1, len(cost)):
        cachedp[i][0] = cachedp[i-1][0] + cost[i][0]

    for r in range(1, len(cost)):
        for c in range(1, len(cost[0])):
            cachedp[r][c] = min(cachedp[r-1][c], cachedp[r][c-1], cachedp[r-1][c-1]) + cost[r][c]

    return cachedp[len(cost) - 1][len(cost[0]) - 1]



print(mincost(cost,2,3))
print(mincostmem(cost, 2,3))
print(mincostdp(cost))

print(mincostdiag(cost,2,3))
print(mincostdiag(cost,2,3))
print(mincostdiagdp(cost))