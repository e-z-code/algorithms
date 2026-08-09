import sys
from collections import deque
INF = float('inf')


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
string = sys.stdin.readline().strip()


# 2. TO CONSTRUCT THE GRAPH

node = [idx for idx in range(length)]
for idx in range(length - 1):
    if string[idx] == "=":
        node[idx+1] = node[idx]

graph = [[] for node in range(length)]
in_degree = [INF for node in range(length)]
for idx in range(length):
    if node[idx] == idx:
        in_degree[idx] = 0

for idx in range(length - 1):
    if string[idx] == ">":
        graph[node[idx+1]].append(node[idx])
        in_degree[node[idx]] += 1
    elif string[idx] == "<":
        graph[node[idx]].append(node[idx+1])
        in_degree[node[idx+1]] += 1


# 3. TOPOLOGICAL SORT

ans = [INF for idx in range(length)]

queue = deque()
for idx in range(length):
    if in_degree[idx] == 0:
        ans[idx] = 1
        queue.append(idx)

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if ans[next_node] == INF:
            ans[next_node] = ans[now_node] + 1
        else:
            ans[next_node] = max(ans[next_node], ans[now_node] + 1)
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

for idx in range(length):
    if ans[idx] == INF:
        ans[idx] = ans[node[idx]]


# 4. TO SOLVE THE PROBLEM

min_sum = 0
for idx in range(length):
    min_sum += arr[idx] * ans[idx]

print(min_sum)
print(" ".join(map(str, ans)))