def lolsszzz(s):
    maxlength = 0
    s = list(map(int, s))
    print(s)
    for i in range(len(s)):
        for j in range(i, len(s)+1, 2):
            # ns = s[i:j]
            k = j-i
            # print(ns)
            if maxlength > k:
                continue
            sumleft, sumright = 0,0
            for p in range(k//2):
                sumleft += s[i+p]
                sumright += s[i+p+k//2]
            # mid = (k - 1) // 2
            # sumleft = sum(ns[:mid + 1])
            # sumright = sum(ns[mid+1:])
            if sumleft == sumright:
                maxlength = k
    return maxlength



def lolss(s):
    maxlength = 0
    s = list(map(int, s))
    print(s)
    for i in range(len(s)):
        for j in range(i, len(s)+1, 2):
            k = j-i
            if maxlength > k:
                continue
            sumleft, sumright = 0,0
            for p in range(k//2):
                sumleft += s[i+p]
                sumright += s[p+k//2]
            if sumleft == sumright:
                maxlength = k
    return maxlength


def lolssdp(s):
    summ = [[0 for x in range(len(s))] for y in range(len(s))]
    s = list(map(int, s))
    n = len(s)
    maxlen = 0
    for i in range(n):
        summ[i][i] = s[i]





print(lolssdp('9430723'))

