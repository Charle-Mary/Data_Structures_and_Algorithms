from collections import  defaultdict
def mincoins(coins, x):
    if x == 0:
        return 0

    res = float('inf')
    for i in range(len(coins)):
        if coins[i] <= x:
            temp = 1 + mincoins(coins, x - coins[i])
            res = min(res, temp)

    return res

cache=defaultdict(int)
def mincoinsmemo(coins, x):
    if x == 0:
        return 0

    if cache[x]:
        return cache[x]

    cache[x] = float('inf')
    for i in range(len(coins)):
        if coins[i] <= x:
            temp = 1 + mincoinsmemo(coins, x - coins[i])
            cache[x] = min(cache[x], temp)

    return cache[x]


def mincoinsdp(coins, x):
    cache = [float('inf') for i in range(x+1)]
    cache[0] = 0

    for i in range(x+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                cache[i] = min(cache[i], 1 + cache[i - coins[j]])
    return cache[-1]

def coinways(coins, x):
    if len(coins) == 0:
        return 0
    if x == 0:
        return 1

    if x < 0:
        return 0

    temp = 0
    for i in range(len(coins)):
        temp += coinways(coins, x - coins[i])

    # return coinways(coins[1:], x) + coinways(coins, x - coins[0])

    return temp

cache1 = defaultdict(int)
def coinwaysmemo(coins, x):
    if x == 0:
        return 1

    if x < 0:
        return 0

    if cache1[x]:
        return cache1[x]

    temp = 0
    for i in range(len(coins)):
        temp += coinways(coins, x - coins[i])
        cache1[x] = temp

    return cache1[x]

def coinwaysdp(coins, x):
    dp = [0 for i in range(x+1)]
    dp[0] = 1

    for i in range(1, x+1):
        for j in range(len(coins)):
            dp[i] += dp[i - coins[j]]
    return dp[-1]









coins = [1,2,3]
#print(mincoins(coins, 20))
# print(mincoinsmemo(coins, 20))
# print(mincoinsdp(coins, 20))
print(coinways(coins, 4))
# print(coinwaysmemo(coins, 11))
#print(coinwaysdp(coins, 20))