import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

a, b, c = map(int, sys.stdin.readline().split())

if b - a == c - b:
    print("secret", b - a)
else:
    print("not secret")