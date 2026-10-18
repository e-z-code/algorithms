import sys


# 2. UNION FIND

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):

    parentX = find(x)
    parentY = find(y)
    if parentX <= parentY:
        parent[parentY] = parentX
    else:
        parent[parentX] = parentY


# 1. TO GET THE INPUT

student_cnt = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))
heights.sort()
inversion_cnt = list(map(int, sys.stdin.readline().split()))
inversion_cnt.sort()


# 3. TO SOLVE THE PROBLEM

possible = True
for idx in range(student_cnt):
    if inversion_cnt[idx] > idx:
        possible = False
        break

if possible:

    ans = [0 for idx in range(student_cnt)]
    parent = [idx for idx in range(student_cnt)]

    for idx in range(student_cnt-1, -1, -1):

        now_height = heights[idx]
        now_inversion_cnt = inversion_cnt[idx]

        init_target = student_cnt - 1 - now_inversion_cnt
        final_target = find(init_target)
        ans[final_target] = now_height
        if final_target != 0:
            union(final_target-1, final_target)

    print(" ".join(map(str, ans)))

else:
    print(-1)