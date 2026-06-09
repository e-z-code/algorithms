import sys


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    book_cnt, move_cnt = map(int, sys.stdin.readline().split())

    # 2. TO SOLVE THE PROBLEM

    if book_cnt == 1:

        print(1)

    elif book_cnt == 2:

        if move_cnt % 2 == 0:
            print(1, 2)
        else:
            print(2, 1)

    else:

        arr = [num for num in range(1, book_cnt + 1)]
        if move_cnt == 0:
            ans = arr
        else:
            if book_cnt > move_cnt:
                ans = list(reversed(arr[-move_cnt:])) + arr[:-move_cnt]
            else:
                ans = list(reversed(arr))
        print(" ".join(map(str, ans)))