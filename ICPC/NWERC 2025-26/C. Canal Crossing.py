import sys
from collections import deque
MAX_EXP = 18

sys.setrecursionlimit(200000)


# 3. LCA FUNCTION

def get_lca(nodeA, nodeB):

    if depths[nodeA] > depths[nodeB]:
        nodeA, nodeB = nodeB, nodeA

    for exp in range(MAX_EXP - 1, -1, -1):
        if depths[nodeB] - depths[nodeA] >= (1 << exp):
            nodeB = parents[nodeB][exp]

    if nodeA == nodeB:
        return nodeA

    for exp in range(MAX_EXP - 1, -1, -1):
        if parents[nodeA][exp] != parents[nodeB][exp]:
            nodeA = parents[nodeA][exp]
            nodeB = parents[nodeB][exp]

    return parents[nodeA][0]


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = [[] for node in range(node_count)]
for edge in range(node_count - 1):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA].append((nodeB, dist))
    graph[nodeB].append((nodeA, dist))


# 2. TO CONSTRUCT THE TREE

depths = [-1 for node in range(node_count)]
children = [[] for node in range(node_count)]
parents = [[-1 for exp in range(MAX_EXP)] for node in range(node_count)]
to_parent = [[-1 for exp in range(MAX_EXP)] for node in range(node_count)]

queue = deque([0])
depths[0] = 0
order = []

while queue:
    now_node = queue.popleft()
    order.append(now_node)
    for next_node, dist in graph[now_node]:
        if depths[next_node] == -1:
            depths[next_node] = depths[now_node] + 1
            children[now_node].append(next_node)
            parents[next_node][0] = now_node
            to_parent[next_node][0] = dist
            queue.append(next_node)

for exp in range(1, MAX_EXP):
    for node in range(node_count):
        if parents[node][exp - 1] != -1:
            parents[node][exp] = parents[parents[node][exp - 1]][exp - 1]
            to_parent[node][exp] = to_parent[node][exp - 1] + to_parent[parents[node][exp - 1]][exp - 1]


# 4. TO SOLVE THE PROBLEM

imos = [0 for node in range(node_count)]

query_count = int(sys.stdin.readline())
for query in range(query_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    imos[nodeA - 1] += 1
    imos[nodeB - 1] += 1
    imos[get_lca(nodeA - 1, nodeB - 1)] -= 2

for node in reversed(order):
    if parents[node][0] != -1:
        imos[parents[node][0]] += imos[node]

ans = 0
for node in range(node_count):
    if imos[node] % 2 == 1:
        ans += to_parent[node][0]
print(ans)