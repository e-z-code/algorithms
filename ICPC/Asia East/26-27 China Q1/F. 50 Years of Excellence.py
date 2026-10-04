import sys


# 1. TO GET THE INPUT

year_cnt, problem_cnt = map(int, sys.stdin.readline().split())

difficulties = [0]
for year in range(year_cnt):
    problems = list(map(int, sys.stdin.readline().split()))
    difficulties.append(sum(problems))


# 2. TO SOLVE THE PROBLEM

ans = 0
for year in range(1, year_cnt + 1):
    if difficulties[year] < difficulties[year-1]:
        ans += 1
print(ans)