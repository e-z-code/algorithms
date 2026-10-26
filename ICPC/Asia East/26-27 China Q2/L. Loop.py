import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))


    # 2. TO SOLVE THE PROBLEM

    ans = float('inf')
    if length == 1:
        ans = arr[0]

    # Forward
    prefix_sum = 0
    for idx in range(length-1):
        result = prefix_sum + arr[idx] * (length-idx) + arr[idx+1] * (length-idx-1)
        prefix_sum += arr[idx] * 2
        ans = min(ans, result)

    # Backward
    prefix_sum = 0
    for idx in range(length-1, 0, -1):
        result = prefix_sum + arr[idx] * idx + arr[(idx+1) % length] * (idx+1)
        prefix_sum += arr[(idx+1) % length] * 2
        ans = min(ans, result)

    print(ans)