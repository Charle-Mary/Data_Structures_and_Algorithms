def retEven(arr):
    if len(arr) == 0:
        return []
    if arr[0] % 2 == 0:
        return [arr[0]] + retEven(arr[1:])
    else:
        return retEven(arr[1:])




X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(retEven(X))
