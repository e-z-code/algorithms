import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

item_cnt, friend_cnt = map(int, sys.stdin.readline().split())

total_price = sum(list(map(int, sys.stdin.readline().split())))
paid_price = sum(list(map(int, sys.stdin.readline().split())))

if total_price * 11 <= paid_price * 10:
    print("YES")
else:
    print("NO")