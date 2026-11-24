import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

task_cnt, slot_cnt = map(int, sys.stdin.readline().split())
tasks = list(map(int, sys.stdin.readline().split()))
tasks.sort()


# 2. TO SOLVE THE PROBLEM

left = max(tasks) * 3 - 1
right = pow(10, 10) * 3

while left + 1 < right:

    goal = (left + right) // 2

    max_one = 0
    max_two = 0
    for task in tasks:
        if task * 5 <= goal:
            max_one += 1
        if task * 10 <= goal:
            max_two += 1

    if max_one:
        if max_two + 2 <= max_one:
            need_slot = max_two + 2 + (max_one - (max_two + 2)) // 2 * 3 + (task_cnt - (max_two + 2) - (max_one - (max_two + 2)) // 2 * 2) * 2
        elif max_two + 1 == max_one:
            need_slot = max_two + 1 + (task_cnt - (max_two + 1)) * 2
        else:
            need_slot = max_two + (task_cnt - max_two) * 2
    else:
        need_slot = 1 + (task_cnt - 1) * 2

    if need_slot > slot_cnt:
        left = goal
    else:
        right = goal

print(right / 3)
