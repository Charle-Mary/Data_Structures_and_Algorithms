def sumChar(arr):
    if len(arr) == 0:
        return 0
    else:
        return len(arr[0]) + sumChar(arr[1:])



X = ["abdhalyr", "c", "def", "ghij", "froir", "riuerwi"]

print(sumChar(X))