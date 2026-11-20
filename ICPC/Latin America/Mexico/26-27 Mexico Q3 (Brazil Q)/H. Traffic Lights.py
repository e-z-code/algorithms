import sys
from collections import deque


# 1. TO GET THE INPUT

light_cnt, switch_cnt = map(int, sys.stdin.readline().split())
lights = list(map(int, sys.stdin.readline().split()))


# 2. MAKE DIFF ARRAY
# diff[idx] = 0 if lights[idx-1] = lights[idx]

diff = []
diff.append(lights[0])
for idx in range(1, light_cnt):
    diff.append(lights[idx-1] ^ lights[idx])
diff.append(lights[-1])


# 3. TO FORM A GRAPH FROM SWITCHES

graph = [[] for idx in range(light_cnt + 1)]
for switch in range(switch_cnt):
    left, right = map(int, sys.stdin.readline().split())
    graph[left-1].append(right)
    graph[right].append(left-1)


# 4. TO SOLVE THE PROBLEM
# A switch (i, j) changes diff[i-1] and diff[j].
# If a connected component has odd numbers of 1 in the diff array, the case is impossible.

ans = "YES"

visited = [0 for idx in range(light_cnt + 1)]
for idx in range(light_cnt + 1):
    if not visited[idx]:

        queue = deque([idx])
        visited[idx] = 1

        result = diff[idx]
        while queue:
            now_idx = queue.popleft()
            for next_idx in graph[now_idx]:
                if not visited[next_idx]:
                    queue.append(next_idx)
                    visited[next_idx] = 1
                    result ^= diff[next_idx]

        if result:
            ans = "NO"
            break

print(ans)