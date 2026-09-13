import sys


# 1. TO GET THE INPUT

while True:

    room_cnt, goal_dist = map(int, sys.stdin.readline().split())
    if room_cnt == 0 and goal_dist == 0:
        break
    rooms = list(map(int, sys.stdin.readline().split()))


    # 2. TO SOLVE THE PROBLEM

    now_cnt = 1
    now_loc = rooms[0] + goal_dist
    for idx in range(1, room_cnt):
        if abs(now_loc - rooms[idx]) <= goal_dist:
            continue
        else:
            now_cnt += 1
            now_loc = rooms[idx] + goal_dist
    print(now_cnt)