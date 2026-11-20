import sys


# 2. BIPARTITE MATCHING FUNCTION

def bipartite_match(idx):

    if visited[idx]:
        return False
    visited[idx] = 1

    for goal_edge in graph[idx]:
        if selected_by[goal_edge] == -1 or bipartite_match(selected_by[goal_edge]):
            selected_by[goal_edge] = idx
            return True
    return False


# 1. TO GET THE INPUT

node_cnt, now_edge_cnt, goal_edge_cnt = map(int, sys.stdin.readline().split())

now_edges = set()
for edge in range(now_edge_cnt):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    if nodeA > nodeB:
        nodeA, nodeB = nodeB, nodeA
    now_edges.add((nodeA, nodeB))

goal_edges = set()
for edge in range(goal_edge_cnt):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    if nodeA > nodeB:
        nodeA, nodeB = nodeB, nodeA
    goal_edges.add((nodeA, nodeB))


# 3. TO SOLVE THE PROBLEM - BIPARTITE MATCHING

intersection = now_edges & goal_edges
now_edges -= intersection
goal_edges -= intersection

if now_edge_cnt != goal_edge_cnt:
    print(-1)
else:

    now_edges = list(now_edges)
    goal_edges = list(goal_edges)

    selected_by = [-1 for idx in range(len(goal_edges))]
    graph = [[] for idx in range(len(now_edges))]
    for now_edge in range(len(now_edges)):
        now_nodeA, now_nodeB = now_edges[now_edge]
        for goal_edge in range(len(goal_edges)):
            goal_nodeA, goal_nodeB = goal_edges[goal_edge]
            if {now_nodeA, now_nodeB} & {goal_nodeA, goal_nodeB}:
                graph[now_edge].append(goal_edge)

    for now_edge in range(len(now_edges)):
        visited = [0 for idx in range(len(now_edges))]
        bipartite_match(now_edge)

    match_cnt = len(selected_by) - selected_by.count(-1)
    print(match_cnt + (len(now_edges) - match_cnt) * 2)