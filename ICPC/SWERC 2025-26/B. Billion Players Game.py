import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length, min_val, max_val = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()


    # 2. TO SOLVE THE PROBLEM

    if length % 2 == 0:
        min_target, max_target = arr[length // 2 - 1], arr[length // 2]
    else:
        min_target, max_target = arr[length // 2], arr[length // 2]

    optimal_val = 0
    if max_val < min_target:
        optimal_val = max_val
    elif max_target < min_val:
        optimal_val = min_val
    else:
        optimal_val = arr[length // 2]

    ans = 0
    for num in arr:
        ans += abs(num - optimal_val)
    print(ans)