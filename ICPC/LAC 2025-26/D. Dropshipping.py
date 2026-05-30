import sys
from heapq import heappush, heappop


# 1. TO GET THE INPUT

item_count, factor, limit = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0

min_heap = []
max_heap = []
counter = dict()

now_idx = item_count - 1
for idx in range(item_count-1, -1, -1):

    while 0 <= now_idx and idx <= now_idx + limit:
        heappush(min_heap, items[now_idx])
        heappush(max_heap, -items[now_idx])
        counter[items[now_idx]] = counter.get(items[now_idx], 0) + 1
        now_idx -= 1

    if (idx + 1) % (factor + 1) == 0:
        while True:
            val = -heappop(max_heap)
            if counter[val] > 0:
                ans += val // 2
                counter[val] -= 1
                break
    else:
        while True:
            val = heappop(min_heap)
            if counter[val] > 0:
                counter[val] -= 1
                break

print(ans)