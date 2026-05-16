import sys
from heapq import heappush, heappop


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

heap = []
for idx in range(length):
    heappush(heap, (arr[idx], idx))

ans = []

for idx in range(length):

    while len(heap) != 0:

        target_num, target_idx = heappop(heap)
        if target_idx <= idx:
            continue
        else:
            if arr[idx] <= target_num:
                heappush(heap, (target_num, target_idx))
                break
            else:
                target_sum = arr[idx] + target_num
                ans.append((idx, target_idx))
                if target_sum % 2 == 0:
                    arr[idx] = target_sum // 2
                    arr[target_idx] = target_sum // 2
                    heappush(heap, (target_sum // 2, target_idx))
                else:
                    arr[idx] = target_sum // 2
                    arr[target_idx] = target_sum // 2 + 1
                    heappush(heap, (target_sum // 2 + 1, target_idx))

print(len(ans))
for i, j in ans:
    print(i+1, j+1)