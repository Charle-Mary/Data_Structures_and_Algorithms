def isInterleaving(a,b,c):
    if not a and not b and not c:
        return True

    if not c:
        return False

    if a and a[0] == c[0]:
        return isInterleaving(a[1:], b, c[1:])
    if b and b[0] == c[0]:
        return isInterleaving(a, b[1:], c[1:])

    return False


def isInterleavingdp(a,b,c):
    m = len(a)
    n = len(b)
    if len(c) != m + n:
        return False

    cache = [[0 for j in range(n+1)] for i in range(m+1)]
    cache[0][0] = True

    for i in range(1, m+1):
        if a[i-1] != c[i-1]:
            cache[i][0] = False
        else:
            cache[i][0] = cache[i-1][0]

    for j in range(1, n+1):
        if b[j-1] != c[j-1]:
            cache[0][j] = False
        else:
            cache[0][j] = cache[0][j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] != c[i+j-1] and b[j-1] != c[i+j-1]:
                cache[i][j] = False
            elif a[i-1] == c[i+j-1] and b[j-1] != c[i+j-1]:
                cache[i][j] = cache[i-1][j]
            elif a[i-1] != c[i+j-1] and b[j-1] == c[i+j-1]:
                cache[i][j] = cache[i][j-1]
            else:
                cache[i][j] = cache[i-1][j] or cache[i][j-1]
    print(cache)
    return cache[-1][-1]

def isInterleavingprint(a,b):
    if not a and not b:
        return [a+b]

    if not a:
        return [b]
    if not b:
        return [a]

    first = isInterleavingprint(a[1:], b)
    second = isInterleavingprint(a, b[1:])

    return [a[0] + f for f in first] + [b[0] + s for s in second]


def isInterleavingNOMATRIX(a,b,c):
    m,n = len(a), len(b)
    i,j = 0, 0
    if len(c) != m+n:
        return False
    for k in range(m+n):
        if i < m and a[i] == c[k]:
            i += 1
        elif j < n and b[j] == c[k]:
            j += 1
        else:
            return False

    if m-1 <= i <= m and n-1 <= j <= n:
        return True
    else:
        return False





a = "bcc"
b = "bbca"
c = "bbcbcac"

#print(isInterleaving(a,b,c))
# print(isInterleavingdp(a,b,c))
#print(isInterleavingprint(a,b))
print(isInterleavingNOMATRIX(a,b,c))