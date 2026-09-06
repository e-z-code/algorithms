import sys
MOD = pow(10, 9) + 7


# 1. PRE-PROCESSING

prefix_sum = [0 for num in range(10 ** 6 + 1)]

for num in range(3, 10 ** 6 + 1):

    odd_cnt, even_cnt = num // 2, num // 2
    if num % 2 == 0:
        even_cnt -= 1

    if num % 2 == 0:
        prefix_sum[num] = (odd_cnt * (odd_cnt - 1)) // 2 + (even_cnt * (even_cnt - 1)) // 2
    else:
        prefix_sum[num] = odd_cnt * even_cnt
    prefix_sum[num] %= MOD

for num in range(1, 10 ** 6 + 1):
    prefix_sum[num] += prefix_sum[num-1]
    prefix_sum[num] %= MOD


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):
    num = int(sys.stdin.readline())
    print(prefix_sum[num])