import collections


def editDistance(s1, s2):
    if len(s1) == 0 or s1 is None:
        return len(s2)
    if len(s2) == 0 or s2 is None:
        return len(s1)
    if s1[0] == s2[0]:
        return editDistance(s1[1:], s2[1:])

    d = 1 + editDistance(s1[1:], s2)
    r = 1 + editDistance(s1[1:], s2[1:])
    i = 1 + editDistance(s1, s2[1:])

    return min(d, r, i)

cache = collections.defaultdict(int)
def editDistanceMemo(s1, s2):
    if (s1,s2) in cache:
        return cache[(s1,s2)]
    elif len(s1) == 0 or s1 is None:
        cache[(s1,s2)] = len(s2)
    elif len(s2) == 0 or s2 is None:
        cache[(s1, s2)] = len(s1)
    elif s1[0] == s2[0]:
        cache[(s1, s2)] = editDistance(s1[1:], s2[1:])

    else:
        d = 1 + editDistance(s1[1:], s2)
        r = 1 + editDistance(s1[1:], s2[1:])
        i = 1 + editDistance(s1, s2[1:])

        cache[(s1, s2)] = min(d,r,i)

    return cache[(s1, s2)]

memo = [[0 for x in range(60)] for y in range(60)]
def editDistancedp(s1, s2):

    for p in range(len(s1) + 1):
        memo[0][p] = p

    for q in range(len(s2) + 1):
        memo[q][0] = q
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
    return memo[len(s1)][len(s2)]


s1 = "sunday"
s2 = "saturday"
print(len(s1), len(s2))

#print(editDistance(s1, s2))
#print(editDistanceMemo(s1,s2))
print(editDistancedp(s1,s2))