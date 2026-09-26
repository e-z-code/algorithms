import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

player_cnt, round_cnt = map(int, sys.stdin.readline().split())

if player_cnt == 2:
    if round_cnt % 2 == 1:
        print("S")
    else:
        print("N")
else:
    if round_cnt == 1:
        print("S")
    else:
        print("N")