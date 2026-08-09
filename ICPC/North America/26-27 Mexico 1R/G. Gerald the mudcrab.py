import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

gem_cnt = int(sys.stdin.readline())
gems = set(list(map(int, sys.stdin.readline().split())))
print(gem_cnt - len(gems))