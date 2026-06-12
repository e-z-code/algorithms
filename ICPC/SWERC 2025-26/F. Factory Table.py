import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))


    # 2. TO SOLVE THE PROBLEM

    decrease = 0
    for idx in range(1, length):
        if arr[idx-1] >= arr[idx]:
            decrease += 1

    if decrease:
        for idx in range(1, length):
            if arr[idx-1] >= arr[idx]:
                print(arr[idx-1] // (arr[idx]-1))
                break
    else:
        print(max(arr[1]-arr[0], arr[-1] // (arr[1]-arr[0])))
