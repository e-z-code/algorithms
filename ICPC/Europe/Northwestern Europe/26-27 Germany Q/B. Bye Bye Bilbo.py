import sys
from heapq import heappush, heappop
INF = float('inf')
sys.setrecursionlimit(200000)


# 2. DFS FUNCTION

def get_depth(now_node, now_depth):

    depth[now_node] = now_depth
    for next_node in graph[now_node]:
        get_depth(next_node, now_depth + 1)


# 1. TO GET THE INPUT

node_cnt, coverage = map(int, sys.stdin.readline().split())
parent = [0] + list(map(int, sys.stdin.readline().split()))
for node in range(node_cnt):
    parent[node] -= 1

graph = [[] for node in range(node_cnt)]
for node in range(1, node_cnt):
    graph[parent[node]].append(node)


# 3. TO SOLVE THE PROBLEM

depth = [INF for node in range(node_cnt)]
get_depth(0, 0)

heap = []
visited = [0 for node in range(node_cnt)]
for node in range(node_cnt):
    if len(graph[node]) == 0:
        heappush(heap, (-depth[node], node))

ans = []
while heap:
    valid = True
    now_depth, now_node = heappop(heap)
    for cnt in range(coverage):
        if visited[now_node]:
            valid = False
            break
        else:
            visited[now_node] = 1
            if now_node == 0:
                ans.append(1)
            else:
                if cnt == coverage - 1:
                    ans.append(now_node + 1)
                now_node = parent[now_node]
                heappush(heap, (-depth[now_node], now_node))

print(len(ans))
print(" ".join(map(str, ans)))