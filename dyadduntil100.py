# def add_until_100(arr):
#     print("RECURSION")
#     if len(arr) == 0:
#         return 0
#     if arr[0] + add_until_100(arr[1:]) > 100:
#         return add_until_100(arr[1:])
#     else:
#         return arr[0] + add_until_100(arr[1:])



# def add_until_100(arr):
#     sum = 0
#     for i in arr:
#         print("ENTER")
#         if  sum + i > 100:
#             return sum
#         else:
#             sum += i


def add_until_100(arr, memo = {}):
    print("RECURSION")
    if len(arr) == 0:
        return 0

    sum_of_remainder = add_until_100(arr[1:])
    if arr[0] + sum_of_remainder > 100:
        return sum_of_remainder
    else:
        return arr[0] + sum_of_remainder





X = [1,2,34,32,2,5,6,5,3,15]
print(add_until_100(X))