import sys


# 1. PREPROCESSING

ans = [-1 for num in range(10 ** 7 + 1)]
ans[0] = 1

for num in range(10 ** 7 + 1):
    if ans[num] == -1:
        ans[num] = ans[num-1] + 1
        now_num, next_num = num, ans[num]
        while next_num <= 10 ** 7:
            ans[next_num] = now_num * 3
            now_num, next_num = next_num, ans[next_num]


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

num = int(sys.stdin.readline())
print(ans[num])