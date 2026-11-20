import sys

dy = [0, 1, 1, 1]
dx = [1, 1, 0, -1]


# 1. TO SOLVE THE PROBLEM

# First move
print(30, 20)
sys.stdout.flush()

# Second move
opp_row, opp_col = map(int, sys.stdin.readline().split())
key_direction = None
for dir in range(4):
    key_arr = [(30+dy[dir], 20+dx[dir]), (30+2*dy[dir], 20+2*dx[dir]), (30-dy[dir], 20-dx[dir])]
    if (opp_row, opp_col) not in key_arr:
        key_direction = dir
        break

print(30+dy[key_direction], 20+dx[key_direction])
sys.stdout.flush()

# Third move
opp_row, opp_col = map(int, sys.stdin.readline().split())
if (30-dy[key_direction], 20-dx[key_direction]) != (opp_row, opp_col):
    print(30-dy[key_direction], 20-dx[key_direction])
    sys.stdout.flush()
else:
    print(30+2*dy[key_direction], 20+2*dx[key_direction])
    sys.stdout.flush()

opp_row, opp_col = map(int, sys.stdin.readline().split())
