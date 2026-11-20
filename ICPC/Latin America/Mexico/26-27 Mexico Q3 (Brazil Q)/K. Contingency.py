import sys


# 1. TO GET THE INPUT

component_cnt = int(sys.stdin.readline())

now_cnt = list(map(int, sys.stdin.readline().split()))
need_cnt = list(map(int, sys.stdin.readline().split()))

total_cnt = sum(now_cnt)


# 2. TO SOLVE THE PROBLEM

ans = -1
for component in range(component_cnt):
    if now_cnt[component] < need_cnt[component]:
        ans = -1
        break
    else:
        ans = max(ans, total_cnt - now_cnt[component] + need_cnt[component])
print(ans)