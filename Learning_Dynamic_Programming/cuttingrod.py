from collections import defaultdict
def crod(arr, n):
     if n <= 0:
          return 0
     maxi = float('-inf')

     for i in range(1, n+1):
          maxi = max(maxi, arr[i] + crod(arr, n-i))

     return maxi
memo = defaultdict(int)
def crodmem(arr,n):
     if n <= 0:
          return 0
     if n in memo:
          return memo[n]

     memo[n] = float('-inf')
     for i in range(1, n+1):
          memo[n] = max(memo[n], arr[i] + crodmem(arr, n-i))

     return memo[n]

def croddp(arr, n):
     dp = [float('-inf') for i in range(n+1)]
     dp[0] = 0
     for i in range(1, n+1):
          for j in range(i+1):
               dp[i] = max(dp[i], arr[j] + dp[i-j])
     return dp[-1]

arr = [0,1,5,8,9,10,17,17,20]
print(crod(arr, 6))
print(crodmem(arr, 6))
print(croddp(arr, 6))