def maxsumsub(arr):
    maxsum = 0

    for i in range(len(arr)):
        tempsum = arr[i]
        for j in range(i+1, len(arr)):
            tempsum += arr[j]
            maxsum = max(tempsum, maxsum)

    return maxsum if maxsum else max(arr)

def maxsumsubrecur(arr):
    n = len(arr) - 1
    if n == 0:
        return arr[-1] if arr[-1] else 0
    maxsum = max(maxsumsubrecur(arr[:n]) + arr[n], arr[n])
    return maxsum

def kadanemaxsum(arr):
    maxsofar = 0
    maxsum = 0

    for i in range(len(arr)):
        maxsofar = maxsofar + arr[i]

        if maxsofar < 0:
            maxsofar = 0
        else:
            maxsum = max(maxsum, maxsofar)
    return maxsum if maxsum else max(arr)


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
X = len(arr) - 1
print(maxsumsub(arr))
print(kadanemaxsum(arr))
print(maxsumsubrecur(arr))