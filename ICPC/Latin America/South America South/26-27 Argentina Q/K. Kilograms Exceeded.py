import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

ans = []
convert = [0, 5, 1, 6, 2, 7, 3, 8, 4]

pw_length = int(sys.stdin.readline())

pw = list(map(int, sys.stdin.readline().split()))
for num in pw:
    ans.append(convert[num])
print(" ".join(map(str, ans)))