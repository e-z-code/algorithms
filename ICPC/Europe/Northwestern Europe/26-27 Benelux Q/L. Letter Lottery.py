import sys
from fractions import Fraction


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

ans = [0 for idx in range(26)]

word_cnt = int(sys.stdin.readline())
for idx in range(word_cnt):
    word = sys.stdin.readline().strip()
    length = len(word)
    for char in word:
        ans[ord(char) - ord('a')] += Fraction(1, word_cnt * length)

print(float(max(ans)))