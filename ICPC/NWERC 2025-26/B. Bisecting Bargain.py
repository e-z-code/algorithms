import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

num = int(sys.stdin.readline())

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

valid_hundreds = [0, 4, 20, 24, 40, 44, 60, 64, 80, 84, 100]
valid_tens = [0, 4]
valid_ones = [0, 4]

units = [500, 200, 100, 50, 20, 10, 5, 2, 1]

if (hundreds in valid_hundreds) and (tens in valid_tens) and (ones in valid_ones):
    print("splittable")
else:

    if num % 2 == 1:
        ans = [1 for cnt in range(num)]
    else:
        ans = []
        if hundreds % 2 == 0 and hundreds % 4 != 0:
            for cnt in range(hundreds // 2):
                ans.append(200)
                num = num % 100
        for unit in units:
            while num >= unit:
                ans.append(unit)
                num -= unit

    print(len(ans))
    print(" ".join(map(str, ans)))