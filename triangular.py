def triang(num):
    if num == 1 or num == 0:
        return num
    else:
        return num + triang(num - 1)



print(triang(998))