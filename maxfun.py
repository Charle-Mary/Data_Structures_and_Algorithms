# def max(arr):
#     print("RECURSION")
#     if len(arr) == 1:
#         return arr[0]
#
#     elif arr[0] > max(arr[1:]):
#         return arr[0]
#     else:
#         return max(arr[1:])


def max(arr):
    print("RECURSION")

    if len(arr) == 1:
        return arr[0]

    max_rem = max(arr[1:])

    if arr[0] > max_rem:
        return arr[0]
    else:
        return max_rem



X = [1,2,3,4,5,65, 67]
print(max(X))