import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

team_cnt, query_cnt = map(int, sys.stdin.readline().split())

roster = {}
for team in range(team_cnt):
    team_name = sys.stdin.readline().strip()
    roster[team_name] = 0

for query in range(query_cnt):
    team_name = sys.stdin.readline().strip()
    if team_name in roster:
        if roster[team_name] == 0:
            print("OK")
            roster[team_name] = 1
        else:
            print("REPEAT")
    else:
        print("WRONG")