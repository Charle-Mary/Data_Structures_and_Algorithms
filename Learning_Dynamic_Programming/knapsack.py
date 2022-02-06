def knapsack(c, weight, val):
    if c <= 0 or len(weight) <= 0:
        return 0

    if weight[0] > c:
        return knapsack(c, weight[1:], val[1:])

    x = val[0] + knapsack(c-weight[0], weight[1:], val[1:])
    y = knapsack(c, weight[1:], val[1:])

    return max(x,y)


def knapsackdp(c, weight, value):
    dp = [[0 for j in range(c+1)] for i in range(len(weight)+1)]

    for i in range(1, len(weight)+1):
        for j in range(1, c+1):
            if weight[i-1] <= j:
                x = j - weight[i-1]
                dp[i][j] = max(value[i-1] + dp[i-1][x], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    m = len(weight)
    n = c
    res = ""
    while m > 0 and n > 0:
        x = dp[m][n]
        if x == dp[m-1][n]:
            m -= 1
            continue
        else:
            res += str(weight[m-1]) + '-'
            x -= value[m-1]
            m -= 1
            n -= weight[m]
    print(res)
    return dp[-1][-1]




weight = [2,3,4,5]
value = [3,4,5,6]
print(knapsack(5,weight, value))
print(knapsackdp(11,weight,value))

