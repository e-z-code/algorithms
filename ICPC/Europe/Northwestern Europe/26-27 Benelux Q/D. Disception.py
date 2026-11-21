import sys


# 1. TO GET THE INPUT

circle_cnt = int(sys.stdin.readline())
circles = list(map(int, sys. stdin.readline().split()))
circles.sort()


# 2. TO SOLVE THE PROBLEM

prefix_sum = [0]
for circle in circles:
    prefix_sum.append(prefix_sum[-1] + circle)

ans = "impossible"
for idx in range(circle_cnt):
    if prefix_sum[idx] >= circles[idx]:
        ans = "possible"
print(ans)