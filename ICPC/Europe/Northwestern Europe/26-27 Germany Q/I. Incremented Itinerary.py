import sys
from collections import deque
INF = float('inf')


# 2. BFS FUNCTION

def bfs(start):

    result = [INF for node in range(node_cnt)]

    result[start] = 0
    queue = deque([start])
    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if result[next_node] == INF:
                result[next_node] = result[now_node] + 1
                queue.append(next_node)

    return result


# 1. TO GET THE INPUT

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

graph = [[] for node in range(node_cnt)]
for edge in range(edge_cnt):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 3. TO SOLVE THE PROBLEM

# To find nodes in the shortest path

dist_from_start = bfs(0)
dist_from_end = bfs(node_cnt - 1)

valid_node = [0 for node in range(node_cnt)]
for node in range(node_cnt):
    if dist_from_start[node] + dist_from_end[node] == dist_from_start[node_cnt-1]:
        valid_node[node] = 1

# To see if an increment is possible

ans = "impossible"
for now_node in range(node_cnt):
    if valid_node[now_node]:
        for next_node in graph[now_node]:
            if dist_from_start[now_node] == dist_from_start[next_node]:
                ans = "possible"

print(ans)