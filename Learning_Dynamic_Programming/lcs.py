s1 = 'abcdef'
s2 = 'abedgkf'
def lcs(s1,s2):
    m = len(s1)
    n = len(s2)

    if m == 0 or n == 0:
        return 0

    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    else:
        return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


cache = [[-1 for j in range(len(s2))] for i in range(len(s1))]

def lcsmemo(s1,s2):
    m = len(s1)
    n = len(s2)

    if m == 0 or n == 0:
        return 0

    if cache[m-1][n-1] != -1:
        return cache[m-1][n-1]

    if s1[-1] == s2[-1]:
        cache[m-1][n-1] = 1 + lcs(s1[:-1], s2[:-1])
    else:
        cache[m-1][n-1] = max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))

    return cache[-1][-1]


def lcsdp(s1,s2):
    cache = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    m = len(s1)
    n = len(s2)
    arr = ""
    while m > 0 and n > 0:
        if s1[m-1] == s2[n-1]:
            arr += s1[m-1]
            m -= 1
            n -= 1
        else:
            if cache[m-1][n] < cache[m][n-1]:
                n -= 1
            else:
                m -= 1
    print(arr[::-1])

    return cache[-1][-1]


def monolcs(arr1, prev, curr):
    if curr == len(arr1):
        return 0

    op1 = 0
    if prev == -1 or arr1[prev] < arr1[curr]:
        op1 = 1 + monolcs(arr1, curr, curr + 1)

    op2 = monolcs(arr1, prev, curr + 1)

    return max(op1,op2)


arr1 = [1,2,3,4,5,4,2,3,7,9,7,3,1,2,4,5,2,1,3,6,8,9,4,2,2,5,90,3,1]
#arr1 = [9,2,-4,-10,-15]
memo = [[0 for j in range(len(arr1))] for i in range(len(arr1))]
def monolcsmemo(arr1, prev, curr):
    if curr == len(arr1):
        return 0

    if prev != -1 and memo[prev][curr] != 0:
        return memo[prev][curr]

    op1 = 0
    if prev == -1 or arr1[prev] < arr1[curr]:
        op1 = 1 + monolcsmemo(arr1, curr, curr + 1)
    op2 = monolcsmemo(arr1, prev, curr + 1)

    if prev != -1:
        memo[prev][curr] = max(op2, op1)

    return max(op1, op2)



def monolisdp(arr1):
    cache = [1 for i in range(len(arr1))]
    lis = [0,0]
    for i in range(1, len(arr1)):
        for j in range(i):
            if arr1[i] > arr1[j]:
                cache[i] = max(cache[i], 1 + cache[j])
                if cache[i] > lis[0]:
                    lis[0] = cache[i]
                    lis[1] = i

    arr = []
    x = lis[0]
    y = lis[1]
    for k in range(y, -1, -1):
        if cache[k] == x:
            arr.append(arr1[k])
            x -= 1
        else:
            continue

    # print(arr1)
    # print(cache)
    # print(arr[::-1])
    return cache

def monoldsdp(arr1):
    cache = [1 for i in range(len(arr1))]
    lds = [0,0]
    for i in reversed(range(len(arr1))):
        for j in reversed(range(i+1, len(arr1))):
            if arr1[i] > arr1[j]:
                cache[i] = max(cache[i], 1 + cache[j])
                if cache[i] > lds[0]:
                    lds[0] = cache[i]
                    lds[1] = i

    arr = []
    x, y = lds
    for k in range(y, len(arr1)):
        if cache[k] == x:
            arr.append(arr1[k])
            x -= 1

    return cache





def lbs(arr):
    cache1 = [1 for i in range(len(arr))]
    cache2 = [1 for j in range(len(arr))]

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache1[i] = max(cache1[i], 1 + cache1[j])

    for i in reversed(range(len(arr))):
        for j in reversed(range(i+1, len(arr))):
            if arr[i] > arr[j]:
                cache2[i] = max(cache2[i], 1 + cache2[j])


    print(cache1)
    print(cache2)

    maxbitonic = [cache1[0] + cache2[0] - 1, 0, 0]

    for k in range(1, len(arr)):
        if cache1[k] + cache2[k] - 1 > maxbitonic[0]:
            maxbitonic[0] = cache1[k] + cache2[k] - 1
            maxbitonic[1] = k
            maxbitonic[2] = k

    arr1 = []
    k = maxbitonic[1]
    for i in range(k, -1, -1):
        if cache1[i] == cache1[k]:
            arr1.append(arr[i])
            k -= 1
    print(arr1)

    arr2 = []
    l = maxbitonic[2]
    for j in range(l, len(arr1)):
        if cache[j] == cache2[l]:
            arr2.append(arr[j])
            l -= 1





    return arr1 + arr2




def maxsum(arr):
    summ= 0
    maxsum = 0
    for i in range(len(arr)):
        summ = max(summ + arr[i], arr[i])
        maxsum = max(summ, maxsum)
    return maxsum

# Y = [-5, -1, -8, -9, 8, -2]
# print(maxsum(Y))
#print(lcs(s1,s2))
#print(lcsmemo(s1,s2))
#print(lcsdp(s1,s2))
# print(monolcs(arr1,-1,0))
# print(monolcsmemo(arr1,-1,0))
#print(monolisdp(arr1))
print(lbs(arr1))
#print(monoldsdp(arr1))