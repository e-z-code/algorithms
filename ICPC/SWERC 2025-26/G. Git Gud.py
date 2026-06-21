import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

target = int(sys.stdin.readline())

ans = []
for mod in range(1, 64):
    for num in range(249999, 0, -1):
        if num % 64 == mod:
            ans.append((num, 1))

for mod in range(1, 64):
    for num in range(249999, 0, -1):
        if num % 64 == 0 and (num // 64) % 64 == mod:
            ans.append((num, min(250000 - num, 64)))

for mod in range(1, 64):
    for num in range(249999, 0, -1):
        if num % 4096 == 0 and (num // 4096) % 64 == mod:
            ans.append((num, min(250000 - num, 4096)))

print(len(ans))
for level, length in ans:
    print(level, length)