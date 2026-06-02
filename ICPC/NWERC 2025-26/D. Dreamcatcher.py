import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

notch_count = int(sys.stdin.readline())

if notch_count % 2 == 0:
    print((notch_count // 4) * 2 - 1)
else:
    print(notch_count // 2)