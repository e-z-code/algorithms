import sys
from heapq import heappush, heappop
INF = float('inf')


# 1. TO GET THE INPUT

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

graph = [[] for node in range(node_cnt)]
for edge in range(edge_cnt):
    nodeA, nodeB, dist, due = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, dist, due))
    graph[nodeB].append((nodeA, dist, due))


# 2. TO SOLVE THE PROBLEM - DIJKSTRA

heap = [(-INF, 0)]
visited = [-1 for node in range(node_cnt)]
visited[0] = INF

while heap:
    now_time, now_node = heappop(heap)
    now_time *= -1
    if now_time >= visited[now_node]:
        for next_node, dist, due in graph[now_node]:
            next_time = min(due, visited[now_node]) - dist
            if next_time > visited[next_node]:
                visited[next_node] = next_time
                heappush(heap, (-next_time, next_node))

ans = []
for node in range(node_cnt):
    if visited[node] >= 0:
        ans.append("1")
    else:
        ans.append("0")
print("".join(ans))