# def fib(num):
#     print("RECURSION")
#     if num == 1 or num == 0:
#         return num
#     else:
#         return fib(num - 2) + fib(num - 1)



def fib(num, memo = {}):
    print("RECURSION")
    if num == 1 or num == 0:
        return num

    if not memo.get(num):
        memo[num] = fib(num - 2, memo) + fib(num - 1, memo)

    return memo[num]



print(fib(5))