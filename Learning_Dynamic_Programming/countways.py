n = 5
def countWays(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return countWays(n-1) + countWays(n-2)

cache = [0] * (n+1)
def countWaysmem(n):
    if cache[n] != 0:
        return cache[n]
    elif n == 0:
        cache[n] = 0
    elif n == 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2

    else:
        cache[n] = countWays(n-1) + countWays(n-2)

    return cache[n]

cachedp = [0] * (n + 1)
def countWaysdp(n):
    cachedp[0] = 0
    cachedp[1] = 1
    cachedp[2] = 2

    for i in range(3, n+1):
        cachedp[i] = cachedp[i-1] + cachedp[i-2]

    return cachedp[n]


def countways3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return 2 * countways3(n-2)




print(countWays(5))
print(countWaysmem(5))
print(countWaysdp(5))
print(countways3(5))