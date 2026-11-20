import sys
from math import sqrt

def get_dist_squared(x1, y1, x2, y2):
    return pow(x1 - x2, 2) + pow(y1 - y2, 2)


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    x1, y1, r1 = map(int, sys.stdin.readline().split())
    x2, y2, r2 = map(int, sys.stdin.readline().split())
    goal = int(sys.stdin.readline())


    # 2. TO SOLVE THE PROBLEM

    dist_squared = get_dist_squared(x1, y1, x2, y2)

    if dist_squared > pow(r1 + r2, 2) or dist_squared <= pow(r1 - r2, 2):
        if goal <= max(2 * r1, 2 * r2):
            print("YES")
        else:
            print("NO")
    else:
        if goal <= sqrt(dist_squared) + r1 + r2:
            print("YES")
        else:
            print("NO")