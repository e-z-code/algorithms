import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    arr_length, goal_length = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    goal = list(map(int, sys.stdin.readline().split()))


    # 2. TO SOLVE THE PROBLEM

    dp = [[0 for goal_idx in range(goal_length + 1)] for arr_idx in range(arr_length + 1)]
    dp[0][0] = 3

    for arr_idx in range(1, arr_length + 1):
        for goal_idx in range(1, goal_length + 1):

            dp[arr_idx][goal_idx] |= (dp[arr_idx-1][goal_idx] & 1)
            if arr_idx >= goal[goal_idx-1]:
                dp[arr_idx][goal_idx] |= min(1, dp[arr_idx - goal[goal_idx-1]][goal_idx-1])

            if arr[arr_idx-1] == goal[goal_idx-1]:
                dp[arr_idx][goal_idx] |= min(2, dp[arr_idx-1][goal_idx-1] << 1)

    if dp[arr_length][goal_length]:
        print("YES")
    else:
        print("NO")
