import sys
from math import log2
INF = float('inf')


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    x = int(sys.stdin.readline())
    key = int(log2(x))

    ans = INF
    for i in range(max(0, key-3), key+3):
        for j in range(61):
            ans = min(ans, abs(pow(2, i) + pow(2, j) - x))
    print(ans)