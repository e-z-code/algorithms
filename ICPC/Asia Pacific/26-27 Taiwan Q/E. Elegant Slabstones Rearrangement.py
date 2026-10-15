import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = []
for row in range(size):
    grid.append(list(map(int, sys.stdin.readline().split())))

# To store start location and goal location

start_loc = [(500, 500)]
for row in range(1, size + 1):
    for col in range(1, size + 1):
        start_loc.append((row, col))

goal_loc = [(500, 500) for idx in range(size * size + 1)]
for row in range(size):
    for col in range(size):
        goal_loc[grid[row][col]] = (row+1, col+1)


# 2. TO SOLVE THE PROBLEM

ans = "Yes"
color = ["X" for cell in range(size * size + 1)]

# To color each cell

for cell in range(1, size * size + 1):
    start_row, start_col = start_loc[cell]
    goal_row, goal_col = goal_loc[cell]
    if start_row == goal_row:
        if start_col != goal_col:
            color[cell] = "R"
    else:
        if start_col == goal_col:
            color[cell]= "B"
        else:
            ans = "No"

for cell in range(1, size * size + 1):
    start_row, start_col = start_loc[cell]
    goal_row, goal_col = goal_loc[cell]
    if color[cell] == "R":
        if start_col > goal_col:
            start_col, goal_col = goal_col, start_col
        for col in range(start_col-1, goal_col):

            if color[grid[start_row-1][col]] == "X":
                color[grid[start_row-1][col]] = "B"
    elif color[cell] == "B":
        if start_row > goal_row:
            start_row, goal_row = goal_row, start_row
        for row in range(start_row-1, goal_row):
            if color[grid[row][start_col-1]] == "X":
                color[grid[row][start_col-1]] = "R"


# To check overlapping

for row in range(size):
    start_grid = []
    goal_grid = []
    for col in range(size):
        num = size * row + col + 1
        if color[num] == "R":
            start_grid.append(num)
        if color[grid[row][col]] == "R":
            goal_grid.append(grid[row][col])
    if start_grid != goal_grid:
        ans = "No"

for col in range(size):
    start_grid = []
    goal_grid = []
    for row in range(size):
        num = size * row + col + 1
        if color[num] == "B":
            start_grid.append(num)
        if color[grid[row][col]] == "B":
            goal_grid.append(grid[row][col])
    if start_grid != goal_grid:
        ans = "No"

print(ans)