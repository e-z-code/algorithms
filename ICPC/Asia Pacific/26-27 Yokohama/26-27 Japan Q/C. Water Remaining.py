import sys


# 1. TO GET THE INPUT

while True:

    length = int(sys.stdin.readline())
    if length == 0:
        break
    depths = list(map(int, sys.stdin.readline().split()))


    # 2. TO SIMULATE THE TANK

    tank = [[1 for depth in range(max(depths))] for idx in range(length)]
    for idx in range(length):
        for depth in range(depths[idx]):
            tank[idx][depth] = 0


    # 3. TO SOLVE THE PROBLEM

    ans = 0
    for depth in range(max(depths)):
        valid = False
        water_cnt = 0
        for idx in range(length):
            if tank[idx][depth] == 0:
                water_cnt += 1
            else:
                if valid:
                    ans += water_cnt
                    water_cnt = 0
                else:
                    valid = True
                    water_cnt = 0
    print(ans)