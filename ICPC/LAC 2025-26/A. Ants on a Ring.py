import sys
from collections import deque
INF = float('inf')


# 1. TO GET THE INPUT

ant_count, length = map(int, sys.stdin.readline().split())
ants = list(map(int, sys.stdin.readline().split()))
goals = list(map(int, sys.stdin.readline().split()))


# 2. TO CHECK POSSIBILITY

ant_order = []
goal_order = []
for idx in range(ant_count):
    ant_order.append([ants[idx], idx])
    goal_order.append([goals[idx], idx])
ant_order.sort()
goal_order.sort()

ant_order = deque(ant_order)
goal_order = deque(goal_order)
while ant_order[0][1] != goal_order[0][1]:
    goal_order.rotate()

possible = True
for idx in range(ant_count):
    if ant_order[idx][1] != goal_order[idx][1]:
        possible = False
        break


# 3. TO SOLVE THE PROBLEM

if possible:

    ant_order = list(ant_order)
    goal_order = list(goal_order)

    for idx in range(1, ant_count):
        if goal_order[idx-1][0] > goal_order[idx][0]:
            goal_order[idx][0] += length

    left_dist = 0
    straight_dist = 0
    right_dist = 0

    for idx in range(ant_count):
        left_dist = max(left_dist, abs(ant_order[idx][0] - (goal_order[idx][0] - length)))
        straight_dist = max(straight_dist, abs(ant_order[idx][0] - goal_order[idx][0]))
        right_dist = max(right_dist, abs(ant_order[idx][0] - (goal_order[idx][0] + length)))

    print(min(left_dist, straight_dist, right_dist))

else:
    print("*")