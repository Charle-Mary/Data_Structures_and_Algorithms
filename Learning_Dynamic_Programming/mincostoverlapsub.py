from collections import defaultdict

cost = [[0,10,75,94], [-1,0,35,50], [-1,-1,0,80], [-1,-1,-1,0]]
memo = defaultdict(tuple)
def calcmincost(s,d):
    if s < 0 or s >= len(cost) or d < 0 or d >= len(cost):
        return "Not valid"
    if s == d or s == d-1:
        return cost[s][d]

    if not memo.get(s,d):
        memo[s][d] = cost[s][d]
        for i in range(s + 1, d):
            temp = calcmincost(s, i) + calcmincost(i, d)
            memo[s][d] = min(memo[s][d], temp)

    return memo[s][d]


def calcmincostdp(cost):
    mincost = [0] * len(cost)

    mincost[0] = 0
    mincost[1] = cost[0][1]

    for i in range(2, len(cost)):
        mincost[i] = cost[0][i]

        for j in range(1, i):
            if mincost[i] > mincost[j] + cost[j][i]:
                mincost[i] = mincost[j] + cost[j][i]

    return mincost[-1]



cache = defaultdict(int)
def noofways(arr, r,c):
    if not cache.get((r,c)):
        if 0 <= r < len(arr) and 0 <= c < len(arr[0]):
            if r == 0 or c == 0:
                cache[(r, c)] = 1

            cache[(r, c)] = noofways(arr, r - 1, c) + noofways(arr, r, c - 1)
        else:
            return 0

    return cache[(r,c)]



print(noofways(cost,2,2))


print(calcmincostdp(cost))