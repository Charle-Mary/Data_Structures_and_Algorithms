def twommgrid(grid, x,y):
    if x == 0 and y == 0 and grid[0][0] == 0:
        return 0
    if x == 0 and grid[0][y] == 0:
        return 1
    if y == 0 and grid[x][0] == 0:
        return 1

    if grid[x][y] == 0:
        return twommgrid(grid, x-1, y) + twommgrid(grid, x, y-1) + twommgrid(grid,x-1,y-1)
    else:
        return 0

def twommgriddp(grid,x,y,m,n):
    cache = [[0 for c in range(m+1)] for r in range(n+1)]

    for i in range(1, n+1):
        if grid[i-1][0] == 0:
            cache[i][0] = 1

    for j in range(1, m+1):
        if grid[0][j-1] == 0:
            cache[0][j] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i-1][j-1] == 0:
                cache[i][j] = cache[i-1][j] + cache[i][j-1] + cache[i-1][j-1]
    return cache[x][y]




grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print(twommgrid(grid,2,2))
print(twommgriddp(grid,2,2,5,5))