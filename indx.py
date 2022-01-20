def indeX(arr):
    if arr[0] == 'x':
        return 0
    return 1 + indeX(arr[1:])




print(indeX('adxfwxg'))

