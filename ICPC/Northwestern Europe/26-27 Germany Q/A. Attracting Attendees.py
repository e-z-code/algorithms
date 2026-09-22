import sys
from collections import deque


# 1. TO GET THE INPUT AND CONSTRUCT THE GRAPH

band_cnt, people_cnt, min_people = map(int, sys.stdin.readline().split())

node_cnt = band_cnt + people_cnt
graph = [[] for node in range(node_cnt)]
for person in range(people_cnt):
    favorite_cnt = int(sys.stdin.readline())
    favorites = list(map(int, sys.stdin.readline().split()))
    for band in favorites:
        graph[band-1].append(band_cnt + person)
        graph[band_cnt + person].append(band-1)


# 2. TO SOLVE THE PROBLEM

join = [1 for node in range(node_cnt)]
degree = [len(graph[node]) for node in range(node_cnt)]

queue = deque()
for band in range(band_cnt):
    if degree[band] < min_people:
        queue.append(band)
        join[band] = 0

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        degree[next_node] -= 1
        if join[next_node]:
            if next_node < band_cnt and degree[next_node] < min_people:
                queue.append(next_node)
                join[next_node] = 0
            else:
                if next_node >= band_cnt and degree[next_node] * 2 < len(graph[next_node]):
                    queue.append(next_node)
                    join[next_node] = 0

ans = []
for band in range(band_cnt):
    if join[band]:
        ans.append(band + 1)

if len(ans) == 0:
    print("impossible")
else:
    print("possible")
    print(len(ans))
    print(" ".join(map(str, ans)))