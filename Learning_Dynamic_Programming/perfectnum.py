def perfectnum(n):
    k = n
    summ = 0
    while k != 0:
        summ += k % 10
        k = k // 10

    return summ


print(perfectnum(67))