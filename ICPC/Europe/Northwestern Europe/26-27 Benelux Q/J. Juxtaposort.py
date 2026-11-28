import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length, pair_cnt = map(int, sys.stdin.readline().split())

score = [0 for idx in range(length)]
for pair in range(pair_cnt):
    idxA, idxB = map(int, sys.stdin.readline().split())
    idxA -= 1
    idxB -= 1
    score[idxA] -= 1
    score[idxB] += 1

arr = []
for idx in range(length):
    arr.append((score[idx], idx+1))
    arr.sort()

ambiguous = False
ans = [arr[0][1]]
for idx in range(1, length):
    if arr[idx][0] == arr[idx-1][0]:
        ambiguous = True
        break
    ans.append(arr[idx][1])

if ambiguous:
    print("ambiguous")
else:
    print(" ".join(map(str, ans)))