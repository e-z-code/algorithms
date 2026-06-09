import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

people_cnt, front_cnt, back_cnt = map(int, sys.stdin.readline().split())

alice = front_cnt + 1
bob = people_cnt - back_cnt
if alice > bob:
    alice, bob = bob, alice

print(max(0, bob - alice - 1))