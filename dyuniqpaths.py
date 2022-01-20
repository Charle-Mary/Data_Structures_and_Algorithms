def uniq_paths(x, y, memo = {}):
    print("RECURSION")
    if x == 1 or y == 1:
        return 1

    if not memo.get((x,y)):
        memo[(x,y)] = uniq_paths(x - 1, y, memo) + uniq_paths(x, y - 1, memo)
    return memo[(x,y)]


print(uniq_paths(3,8))