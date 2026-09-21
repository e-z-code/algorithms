import sys
INF = float('inf')

blocks = [
    [(-1, 0), (0, 0), (-1, -1)], [(-1, 0), (0, 0), (-1, 1)], [(0, 1), (0, 0), (-1, 1)], [(0, 1), (0, 0), (1, 1)],
    [(1, 0), (0, 0), (1, 1)], [(1, 0), (0, 0), (1, -1)], [(0, -1), (0, 0), (1, -1)], [(0, -1), (0, 0), (-1, -1)],
    [(0, 0), (-1, 0), (0, 1)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 0), (0, -1)], [(0, 0), (0, -1), (-1, 0)]
]


# 1. A FUNCTION TO SOLVE THE PROBLEM

def fill(row, col):

    fill_idx = INF

    for block_idx in range(12):
        valid = True
        for dy, dx in blocks[block_idx]:
            if ans[row+dy][col+dx] != ".":
                valid = False
                break
        if valid:
            fill_idx = block_idx
            break

    fill_block = blocks[fill_idx]
    for idx in range(3):
        dy, dx = fill_block[idx]
        if idx == 0:
            ans[row+dy][col+dx] = "O"
        else:
            ans[row+dy][col+dx] = "#"


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

goal = int(sys.stdin.readline())

# Make empty field

length = 1
while length * length <= goal:
    length += 1
length -= 1

ans = [["." for col in range(100)] for row in range(100)]
for row in range(2, 2 + length):
    for col in range(2, 2 + length):
        ans[row][col] = "F"

goal -= length * length
for col in range(2, 2 + length):
    if goal == 0:
        break
    ans[2+length][col] = "F"
    goal -= 1
for row in range(2, 2 + length):
    if goal == 0:
        break
    ans[row][2+length] = "F"
    goal -= 1

# Make boundaries

for row in range(1, 2 + length + 2):
    for col in range(1, 2 + length + 2):
        if ans[row][col] == ".":
            fill(row, col)

# Print answer

for row in range(100):
    for col in range(100):
        if ans[row][col] == "F":
            ans[row][col] = "."

print(100, 100)
for line in ans:
    print("".join(line))