import sys
from collections import deque
INF = float('inf')


# 1. TO GET THE INPUT

friend_cnt, card_cnt = map(int, sys.stdin.readline().split())

friend_to_idx = {}
guest_cnt = [-1 for idx in range(card_cnt)]
for idx in range(card_cnt):
    friend, guest = map(int, sys.stdin.readline().split())
    friend_to_idx[friend] = idx
    guest_cnt[idx] = guest

graph = [[] for idx in range(card_cnt)]
accepted = [-1 for idx in range(card_cnt)]
visit_info = [(-1, -1) for idx in range(card_cnt)]
for idx in range(card_cnt):
    info = list(sys.stdin.readline().split())
    if info[0] == "A":
        start, end = int(info[1]), int(info[2])
        accepted[idx] = 1
        visit_info[idx] = (start, start + end)
    elif info[0] == "D":
        accepted[idx] = 0
        visit_info[idx] = (INF, INF)
    else:
        friend = int(info[1])
        if friend in friend_to_idx:
            graph[friend_to_idx[friend]].append(idx)


# 2. TO CHECK WHO COMES

queue = deque([])
for idx in range(card_cnt):
    if accepted[idx] == 1:
        queue.append(idx)

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if accepted[next_node] == -1:
            queue.append(next_node)
            accepted[next_node] = 1
            visit_info[next_node] = visit_info[now_node]


# 3. TO SOLVE THE PROBLEM

event = {}
for idx in range(card_cnt):
    if accepted[idx] == 1:
        start, end = visit_info[idx]
        event[start] = event.get(start, 0) + guest_cnt[idx]
        event[end] = event.get(end, 0) - guest_cnt[idx]

timeline = []
for time in event:
    timeline.append((time, event[time]))
timeline.sort()

max_capacity = 0
now_capacity = 0
for time, change in timeline:
    now_capacity += change
    max_capacity = max(max_capacity, now_capacity)
print(max_capacity)