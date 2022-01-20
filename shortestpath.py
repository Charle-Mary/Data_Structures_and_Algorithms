def shortPaths(x, y):
    if x == 1 or y == 1:
        return 1
    return shortPaths(x - 1, y) + shortPaths(x, y - 1)


print(shortPaths(12, 12))