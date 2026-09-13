import sys


# 1. TO GET THE INPUT

while True:

    bottle_cnt = int(sys.stdin.readline())
    if bottle_cnt == 0:
        break

    bottles = []
    for bottle in range(bottle_cnt):
        price, gem = tuple(map(int, sys.stdin.readline().split()))
        bottles.append((price, gem))
    bottles.sort()


    # 2. TO SOLVE THE PROBLEM

    gem_cnt = 0
    for price, gem in bottles:
        gem_cnt += gem

    ans = 0
    left_cnt = max(1, bottle_cnt - gem_cnt)
    bought = [0 for idx in range(bottle_cnt)]
    for idx in range(bottle_cnt):
        price, gem = bottles[idx]
        if gem:
            ans += price
            left_cnt -= 1
            bought[idx] = 1
            break

    for idx in range(bottle_cnt):
        price, gem = bottles[idx]
        if left_cnt and not bought[idx]:
            ans += price
            left_cnt -= 1
            bought[idx] = 1

    print(ans)