import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

level_cnt = int(sys.stdin.readline())

index = []

total_buy = 0
total_sell = 0
for level in range(level_cnt):
    buy, sell = map(int, sys.stdin.readline().split())
    total_buy += buy
    total_sell += sell
    if total_buy > total_sell:
        index.append("COMPRA")
    elif total_buy == total_sell:
        index.append("NEUTRO")
    else:
        index.append("VENDA")

query_cnt = int(sys.stdin.readline())
for query in range(query_cnt):
    level = int(sys.stdin.readline())
    print(index[level - 1])