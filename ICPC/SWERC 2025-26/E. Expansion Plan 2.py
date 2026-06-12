import sys


# 1. TO GET THE INPUT

length, query_cnt = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())


# 2. PREFIX SUM

prefix_sum = [[0, 0] for idx in range(length + 1)]

for idx in range(length):
    if arr[idx] == "4":
        prefix_sum[idx+1][0] = 1
    else:
        prefix_sum[idx+1][1] = 1

for idx in range(1, length + 1):
    prefix_sum[idx][0] += prefix_sum[idx-1][0]
    prefix_sum[idx][1] += prefix_sum[idx-1][1]


# 3. TO GET THE ANSWER

for query in range(query_cnt):

    left, right, x, y = map(int, sys.stdin.readline().split())
    x, y = abs(x), abs(y)

    four_left, eight_left = prefix_sum[right][0] - prefix_sum[left-1][0], prefix_sum[right][1] - prefix_sum[left-1][1]

    eight_used = min(x, y, eight_left)
    x -= eight_used
    y -= eight_used
    eight_left -= eight_used

    if x + y <= four_left + eight_left:
        print("YES")
    else:
        print("NO")