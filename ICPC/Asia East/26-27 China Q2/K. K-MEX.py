import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()


    # 2. TO GET POSSIBLE K-MEX

    leftover = {}
    default_mex = 0
    for num in arr:
        if num == default_mex:
            default_mex += 1
        else:
            leftover[num] = leftover.get(num, 0) + 1

    possible_k = set()
    now_mex = default_mex
    for num in leftover:
        possible_k.add(default_mex + num)

    k_mex = {}
    while True:

        to_delete = set()
        for k in possible_k:

            count = 0
            if now_mex in leftover:
                count += leftover[now_mex]
            if k - now_mex in leftover:
                count += leftover[k - now_mex]
            if 0 <= k - now_mex < default_mex:
                count += 1

            valid = True
            if k < now_mex:
                if count < 1:
                    valid = False
            else:
                if k - now_mex <= now_mex:
                    if count < 2:
                        valid = False
                elif k - now_mex > now_mex:
                    if count < 1:
                        valid = False

            if not valid:
                to_delete.add(k)
                k_mex[k] = now_mex

        possible_k -= to_delete
        if not possible_k:
            break

        now_mex += 1


    # 3. TO SOLVE THE PROBLEM

    ans = 0

    query_cnt = int(sys.stdin.readline())
    for idx in range(query_cnt):
        query = int(sys.stdin.readline())
        ans ^= k_mex.get(query, default_mex)

    print(ans)