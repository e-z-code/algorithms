import sys


# 2. FUNCTIONS TO SOLVE THE PROBLEM

def flip(grid):

    result = [[0 for col in range(col_cnt)] for row in range(row_cnt)]
    for row in range(row_cnt):
        for col in range(col_cnt):
            result[row][col] = grid[row][col_cnt-1-col]
    return result

def rotate90(grid):

    result = [[0 for col in range(col_cnt)] for row in range(row_cnt)]
    for row in range(row_cnt):
        for col in range(col_cnt):
            result[row][col] = grid[size-1-col][row]
    return result

def rotate180(grid):

    result = [[0 for col in range(col_cnt)] for row in range(row_cnt)]
    for row in range(row_cnt):
        for col in range(col_cnt):
            result[row][col] = grid[row_cnt-1-row][col_cnt-1-col]
    return result

def valid(gridA, gridB):

    result = 1
    for row in range(row_cnt):
        for col in range(col_cnt):
            if gridA[row][col] != gridB[row][col]:
                result = 0
    return result


# 1. TO GET THE INPUT

row_cnt, col_cnt = map(int, sys.stdin.readline().split())
if row_cnt == col_cnt:
    size = row_cnt

grid = []
for row in range(row_cnt):
    grid.append(list(sys.stdin.readline().strip()))


# 3. TO SOLVE THE PROBLEM

ans = 1
copy_grid = [[grid[row][col] for col in range(col_cnt)] for row in range(row_cnt)]

if row_cnt == col_cnt:
    for rotate in range(3):
        copy_grid = rotate90(copy_grid)
        ans += valid(grid, copy_grid)
else:
    copy_grid = rotate180(copy_grid)
    ans += valid(grid, copy_grid)

copy_grid = flip(copy_grid)
ans += valid(grid, copy_grid)

if row_cnt == col_cnt:
    for rotate in range(3):
        copy_grid = rotate90(copy_grid)
        ans += valid(grid, copy_grid)
else:
    copy_grid = rotate180(copy_grid)
    ans += valid(grid, copy_grid)

print(ans)
