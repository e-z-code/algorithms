import sys
from collections import deque


# 1. TO GET THE INPUT

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

graph = [[] for node in range(node_cnt)]
for edge in range(edge_cnt):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 2. TO SOLVE THE PROBLEM

parent = [node_cnt for node in range(node_cnt)]
children = [[] for node in range(node_cnt)]

parent[0] = 0
queue = deque([0])
while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if parent[next_node] == node_cnt:
            parent[next_node] = now_node
            children[now_node].append(next_node)
            queue.append(next_node)

ans = 0
for node in range(node_cnt):
    if len(children[node]) == 0:
        ans += 1
print(ans)