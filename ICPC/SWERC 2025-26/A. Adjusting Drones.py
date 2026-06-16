import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length, limit = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))


    # 2. TO SOLVE THE PROBLEM

    ans = 0

    counter = {}
    for num in arr:
        counter[num] = counter.get(num, 0) + 1

    keys = list(sorted(counter.keys()))

    ans = 0
    now_ans = 0

    for idx in range(len(keys)):

        op_needed = max(0, counter[keys[idx]] - limit)
        if idx == len(keys) - 1:
            now_ans += op_needed
            ans = max(ans, now_ans)
        else:
            dist = keys[idx+1] - keys[idx]
            if dist <= op_needed:
                now_ans += dist
                counter[keys[idx+1]] += counter[keys[idx]] - dist
            else:
                now_ans += op_needed
                ans = max(ans, now_ans)
                now_ans = 0

    print(ans)