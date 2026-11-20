import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

total_length, palindrome_length = map(int, sys.stdin.readline().split())

ans = []
leftover = "bcdefghijklmnopqrstuvwxyz"
for idx in range(palindrome_length):
    ans.append("a")
for idx in range(total_length - palindrome_length):
    ans.append(leftover[idx % 25])

print("".join(ans))

