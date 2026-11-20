import sys
INF = float('inf')


# 1. TO GET THE INPUT

card_cnt = int(sys.stdin.readline())
card_cnt += 1

cardsA = [0] + list(map(int, sys.stdin.readline().split()))
cardsB = [0] + list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM - DP

dpA = [0 for idx in range(card_cnt)]
dpB = [0 for idx in range(card_cnt)]

bestA = -INF
bestB = INF
for idx in range(card_cnt-1, -1, -1):
    dpA[idx] = max(bestA, min(cardsA[idx], bestB))
    dpB[idx] = min(bestB, max(cardsB[idx], bestA))
    bestA = max(bestA, dpA[idx])
    bestB = min(bestB, dpB[idx])

print(dpA[0])