import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

a, b = map(int, sys.stdin.readline().split())
memory = int(sys.stdin.readline())

num = 1
now_memory = 0

while True:
    if num % a == 0:
        if num % b == 0:
            now_memory += 8
        else:
            now_memory += 4
    else:
        if num % b == 0:
            now_memory += 4
        else:
            now_memory += len(str(num))
    if now_memory > memory:
        print(num - 1)
        break
    num += 1