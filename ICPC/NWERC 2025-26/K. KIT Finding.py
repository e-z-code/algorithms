import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

height, width, k_cnt, i_cnt, t_cnt = map(int, sys.stdin.readline().split())

ans = [["" for col in range(width)] for row in range(height)]
order = ["K", "I", "T"] + ["K"] * (k_cnt - 1) + ["T"] * (t_cnt - 1) + ["I"] * (i_cnt - 1)

idx = 0
for row in range(height):
    for col in range(width):
       ans[row][col] = order[idx]
       idx += 1

for line in ans:
    print("".join(line))