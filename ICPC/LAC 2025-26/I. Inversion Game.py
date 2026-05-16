import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

odd_appearance = set()
for num in arr:
    if num in odd_appearance:
        odd_appearance.remove(num)
    else:
        odd_appearance.add(num)

if len(odd_appearance) <= 1:
    print("E")
else:
    if len(odd_appearance) % 2 == 0:
        print("F")
    else:
        print("S")