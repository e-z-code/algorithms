import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

exchange_rate, local_cost, abroad_cost = map(int, sys.stdin.readline().split())
print(min(exchange_rate * abroad_cost, local_cost))