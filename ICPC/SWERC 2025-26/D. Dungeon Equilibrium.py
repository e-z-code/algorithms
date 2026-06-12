import sys


# 1. TO GET THE INPUT

monster_cnt = int(sys.stdin.readline())
monsters = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

counter = [0 for level in range(1001)]
for monster in monsters:
    counter[monster] += 1

ans = 0
for level in range(1001):
    if counter[level] != 0:
        if counter[level] < level:
            ans += counter[level]
        else:
            ans += counter[level] - level
print(ans)
