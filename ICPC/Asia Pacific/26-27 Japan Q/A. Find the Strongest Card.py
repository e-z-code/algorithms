import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

strength = [2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]

while True:

    card_cnt = int(sys.stdin.readline())
    if card_cnt == 0:
        break

    now_best = 3
    cards = list(map(int, sys.stdin.readline().split()))
    for card in cards:
        if strength.index(card) < strength.index(now_best):
            now_best = card
    print(now_best)