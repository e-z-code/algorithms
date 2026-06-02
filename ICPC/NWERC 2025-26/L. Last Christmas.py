import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

rank_count = int(sys.stdin.readline())

count = {}
score = {}
singers = set()

for rank_num in range(rank_count):
    rank = list(sys.stdin.readline().strip().split())
    for idx in range(10):
        singer = rank[idx]
        count[singer] = count.get(singer, 0) + 1
        score[singer] = score.get(singer, 0) + pow(1000, 9 - idx)
        singers.add(singer)

singers = list(singers)
singers.sort(key = lambda x : (-count[x], -score[x], x))

if 1 < len(singers) and count[singers[0]] == count[singers[1]] and score[singers[0]] == score[singers[1]]:
    print("tie")
else:
    print(singers[0])