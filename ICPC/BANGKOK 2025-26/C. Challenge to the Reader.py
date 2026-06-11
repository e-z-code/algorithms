import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):

    goal = int(sys.stdin.readline())

    opposite = False
    if goal < 1:
        opposite = True
        goal = 2 - goal


    # 2. TO GET THE MINIMUM LENGTH

    if goal == 1:
        now_num = 1
        now_sum = 1
    else:
        now_num = 2
        now_sum = 1
        while True:
            now_sum += now_num
            if now_sum >= goal:
                diff = now_sum - goal
                if diff % 2 == 0 and diff // 2 != 1 and diff // 2 != now_sum - 1:
                    break
            now_num += 1

    print(now_num)


    # 3. TO CONSTRUCT THE ANSWER

    ans = ["+" for num in range(now_num + 1)]

    diff = (now_sum - goal) // 2

    now_idx = now_num
    while diff != 0:
        if now_idx <= diff and diff - now_idx != 1:
            ans[now_idx] = "-"
            diff -= now_idx
        now_idx -= 1

    if opposite:
        for idx in range(2, now_num + 1):
            if ans[idx] == "+":
                ans[idx] = "-"
            else:
                ans[idx] = "+"

    print(1, end = "")
    for num in range(2, now_num + 1):
        print(ans[num], end = "")
        print(num, end= "")
    print()
