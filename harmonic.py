def harmonics(num):
    if num == 1:
        return 1
    else:
        return (1 / num) + harmonics(num - 1)



print(harmonics(5))