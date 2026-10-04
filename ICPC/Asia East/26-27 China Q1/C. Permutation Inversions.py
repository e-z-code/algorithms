import sys
from heapq import heappop, heappush


# 1. TO GET THE INPUT

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    length, query_cnt = map(int, sys.stdin.readline().split())

    graph = [set() for idx in range(length+1)]
    in_degree = [0 for idx in range(length+1)]

    for query in range(query_cnt):
        result = list(map(int, sys.stdin.readline().split()))
        if result[0] != result[1]:
            for i in range(2, len(result)-1):
                if result[i+1] not in graph[result[i]]:
                    graph[result[i]].add(result[i+1])
                    in_degree[result[i+1]] += 1


    # 2. TO SOLVE THE PROBLEM - TOPOLOGICAL SORT

    now_num = 1
    ans = [0 for idx in range(length)]

    t_sort = []
    for idx in range(1, length+1):
        if in_degree[idx] == 0:
            heappush(t_sort, idx)

    while t_sort:
        now_idx = heappop(t_sort)
        ans[now_idx-1] = now_num
        now_num += 1
        for next_idx in graph[now_idx]:
            in_degree[next_idx] -= 1
            if in_degree[next_idx] == 0:
                heappush(t_sort, next_idx)

    if min(ans) == 0:
        print(-1)
    else:
        print(" ".join(map(str, ans)))