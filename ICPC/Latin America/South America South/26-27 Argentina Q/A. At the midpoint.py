import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

hour, minute, second = map(int, sys.stdin.readline().split())

if hour < 2:
    print("-")
elif hour == 2:
    if minute < 30:
        print("-")
    elif minute == 30:
        if second == 0:
            print("=")
        else:
            print("+")
    else:
        print("+")
else:
    print("+")