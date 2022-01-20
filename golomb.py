def golomb(num, memo={}):
    print("RECURSION")
    if num == 1:
        return 1
    if not memo.get(num):
        memo[num] = 1 + golomb(num - golomb(golomb(num - 1, memo), memo), memo)
    return memo[num]




print(golomb(7))