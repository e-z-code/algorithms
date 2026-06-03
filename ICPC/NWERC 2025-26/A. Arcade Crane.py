import sys
from collections import deque
from itertools import permutations

def get_next(perm, i, j):
    a, b, c, d, e = perm
    if (i, j) == (1, 2):
        return (d, a, b, c, e)
    elif (i, j) == (1, 3):
        return (d, e, a, b, c)
    elif (i, j) == (2, 1):
        return (b, c, d, a, e)
    elif (i, j) == (2, 3):
        return (a, e, b, c, d)
    elif (i, j) == (3, 1):
        return (c, d, e, a, b)
    else:
        return (a, c, d, e, b)


# 1. PRE-PROCESSING FOR LENGTH 5

num = 0
perm_to_num = {}
for perm in permutations(range(1, 6), 5):
    perm_to_num[perm] = num
    num += 1

start_perm = (1, 2, 3, 4, 5)
queue = deque([start_perm])
visited = [[] for num in range(120)]
visited[perm_to_num[start_perm]] = [(1, 1)]
while queue:
    now_perm = queue.popleft()
    for i, j in ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)):
        next_perm = get_next(now_perm, i, j)
        if len(visited[perm_to_num[next_perm]]) == 0:
            visited[perm_to_num[next_perm]] = visited[perm_to_num[now_perm]] + [(i, j)]
            queue.append(next_perm)


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

doll_count = int(sys.stdin.readline())
dolls = list(map(int, sys.stdin.readline().split()))

ans = []

target_doll = doll_count
while target_doll != 5:
    target_idx = dolls.index(target_doll)
    if target_idx <= 1:
        ans.append((1, target_doll-2))
        dolls = dolls[3:target_doll] + dolls[0:3] + dolls[target_doll:]
        target_idx = dolls.index(target_doll)
    if target_idx != target_doll-1:
        ans.append((target_idx-1, target_doll-2))
        dolls = dolls[:target_idx-2] + dolls[target_idx+1:target_doll] + dolls[target_idx-2:target_idx+1] + dolls[target_doll:]
    target_doll -= 1

final_tuple = tuple(dolls[:5])
final_visited = reversed(visited[perm_to_num[final_tuple]])
for i, j in final_visited:
    ans.append((j, i))

print(len(ans))
for i, j in ans:
    print(i, j)