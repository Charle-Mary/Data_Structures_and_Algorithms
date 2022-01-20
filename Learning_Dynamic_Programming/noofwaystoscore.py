from collections import defaultdict
def scoreways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return scoreways(n-10) + scoreways(n - 5) + scoreways(n - 3)

cache = defaultdict(int)
cachedup = defaultdict(tuple)
def scorewaysmem(n):
    if n in cache:
        return cache[n]
    elif n < 0:
        cache[n] = 0
    elif n == 0:
        cache[n] = 1
    else:

        cache[n] = scorewaysmem(n - 10) + scorewaysmem(n - 5) + scorewaysmem(n - 3)


    return cache[n]


def scorewaysdp(n):
    cachedp = [0] * (n + 1)

    cachedp[0] = 1

    for i in range(1, n+1):
        if i - 3 >= 0:
            cachedp[i] += cachedp[i-3]
        if i - 5 >= 0:
            cachedp[i] += cachedp[i-5]
        if i - 10 >= 0:
            cachedp[i] += cachedp[i-10]

    return cachedp[n]

def scorewaysdpdup(n):
    cachedp = [0] * (n + 1)

    cachedp[0] = 1

    for i in range(1, n + 1):
        if i - 3 >= 0:
            cachedp[i] += cachedp[i-3]
    for i in range(1, n + 1):
        if i - 5 >= 0:
            cachedp[i] += cachedp[i-5]
    for i in range(1, n + 1):
        if i - 10 >= 0:
            cachedp[i] += cachedp[i-10]

    return cachedp[n]





print(scoreways(8))
print(scorewaysmem(100))
print(scorewaysdp(100))
print(scorewaysdpdup(8))