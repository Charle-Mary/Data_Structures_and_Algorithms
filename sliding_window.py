import collections


def sliding_window(nums, k):
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output


def coinchange(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]

    dp[0] = 0

    for i in range(len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return -1 if dp[-1] == float('inf') else dp[-1]
from collections import defaultdict
def calcEquation(equations, values, queries):
    graph = defaultdict(dict)
    N = len(equations)

    for i in range(N):
        graph[equations[i][0]][equations[i][1]] = values[i]
        graph[equations[i][1]][equations[i][0]] = 1 / values[i]

    print(graph)
    def dfs(x, y, visited):
        if x not in graph or y not in graph:
            return -1

        if y in graph[x]:
            return graph[x][y]

        for i in graph[x]:
            if i not in visited:
                visited.add(i)
                temp = dfs(i, y, visited)
                if temp == -1:
                    continue
                else:
                    return temp * graph[x][i]
        return -1

    output = []
    for p, q in queries:
        output.append(dfs(p, q, set()))

        return output

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# print(sliding_window([1,3,-1,-3,5,3,6,7], 3))

calcEquation(equations, values, queries)