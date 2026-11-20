import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    c_cnt, h_cnt, o_cnt = map(int, sys.stdin.readline().split())

    if h_cnt == 2 * c_cnt - 4:
        print("Saturated")
    else:
        print("Unsaturated")